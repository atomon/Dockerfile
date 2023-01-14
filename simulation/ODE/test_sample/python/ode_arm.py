#!/usr/bin/python
# -*- coding: utf-8 -*-

# oを長押しで，円軌道
# x, y, zを押した回数分その軸方向に移動
# X, y, Zを押した回数分その軸のマイナス方向に移動


import odepy
import drawstuffpy as ds
import ctypes
import numpy as np

def Main():
    world, space, ground, contactgroup = CreateWorld()

    # 3 自由度ロボットアーム
    robot = Robot(world, space)

    def __StepCallback(pause):

        # 関節値の PD 制御
        tDelta = 0.01
        robot.Control(tDelta)

        # 目標値と現在値の確認
        posTarget = robot.GetTargetPos()
        pos = robot.GetManipPos()
        err = 0.0
        for target, current in zip(posTarget, pos):
            err += abs(target - current)
        print(err)

        odepy.dWorldStep(world, tDelta)
        odepy.dJointGroupEmpty(contactgroup)

        for geom in robot.GetGeoms():
            r = odepy.dReal()
            l = odepy.dReal()
            if odepy.dGeomGetClass(geom) == odepy.dCylinderClass:
                odepy.dGeomCylinderGetParams(geom, ctypes.byref(r), ctypes.byref(l))
                ds.dsDrawCylinderD(odepy.dGeomGetPosition(geom), odepy.dGeomGetRotation(geom), l.value, r.value)
            if odepy.dGeomGetClass(geom) == odepy.dCapsuleClass:
                odepy.dGeomCapsuleGetParams(geom, ctypes.byref(r), ctypes.byref(l))
                ds.dsDrawCapsuleD(odepy.dGeomGetPosition(geom), odepy.dGeomGetRotation(geom), l.value, r.value)

    def __Command(cmd):

        if chr(cmd) == 'o':
            # 円軌道に沿って移動します。
            robot.MoveCircleTrajectory()
            return

        x, y, z = robot.GetTargetPos()
        if chr(cmd) == 'x':
            x += 0.1
        if chr(cmd) == 'X':
            x -= 0.1
        if chr(cmd) == 'y':
            y += 0.1
        if chr(cmd) == 'Y':
            y -= 0.1
        if chr(cmd) == 'z':
            z += 0.1
        if chr(cmd) == 'Z':
            z -= 0.1

        lBase, l1, l2, l3, lManip = robot.GetLinkLengthList()

        if z < lManip / 2.0:
            return

        # 解が存在しない入力を無視します。
        pos0 = np.array([0, 0, l1 + lBase], dtype=np.float64)
        posTarget = np.array([x, y, z], dtype=np.float64)
        if np.linalg.norm(posTarget - pos0) > l2 + l3:
            return
        robot.SetTargetPos(posTarget)

    RunDrawStuff(__StepCallback, __Command)
    DestroyWorld(world, space)

class Robot(object):

    def __init__(self, world, space, lBase=0.10, l1=0.90, l2=1.0, l3=1.0, lManip=0.10):

        self.__lBase = lBase
        self.__l1 = l1
        self.__l2 = l2
        self.__l3 = l3
        self.__lManip = lManip

        # ジオメトリの作成
        q = odepy.dQuaternion()
        odepy.dQFromAxisAndAngle(q, 0, 0, 1, 0.0)
        self.__base = self.__AddCylinder(world, space, r=0.20, l=lBase, m=9.0, px=0.0, py=0.0, pz=(lBase / 2.0), q=q)
        self.__link1 = self.__AddCapsule(world, space, r=0.04, l=l1, m=2.0, px=0.0, py=0.0, pz=(lBase + l1 / 2.0), q=q)
        self.__link2 = self.__AddCapsule(world, space, r=0.04, l=l2, m=2.0, px=0.0, py=0.0, pz=(lBase + l1 + l2 / 2.0), q=q)
        self.__link3 = self.__AddCapsule(world, space, r=0.04, l=l3, m=2.0, px=0.0, py=0.0, pz=(lBase + l1 + l2 + l3 / 2.0), q=q)
        self.__manip = self.__AddCylinder(world, space, r=0.02, l=lManip, m=0.5, px=0.0, py=0.0, pz=(lBase + l1 + l2 + l3 + lManip / 2.0), q=q)

        # 地面に固定します。
        self.__jointBase = odepy.dJointCreateFixed(world, 0)
        odepy.dJointAttach(self.__jointBase, odepy.dGeomGetBody(self.__base), 0)
        odepy.dJointSetFixed(self.__jointBase)

        self.__joint1 = self.__AddJoint(world, odepy.dGeomGetBody(self.__base), odepy.dGeomGetBody(self.__link1), [0.0, 0.0, lBase], [0, 0, 1])
        self.__joint2 = self.__AddJoint(world, odepy.dGeomGetBody(self.__link1), odepy.dGeomGetBody(self.__link2), [0.0, 0.0, lBase + l1], [0, 1, 0])
        self.__joint3 = self.__AddJoint(world, odepy.dGeomGetBody(self.__link2), odepy.dGeomGetBody(self.__link3), [0.0, 0.0, lBase + l1 + l2], [0, 1, 0])

        # マニピュレータ
        self.__jointManip = odepy.dJointCreateFixed(world, 0)
        odepy.dJointAttach(self.__jointManip, odepy.dGeomGetBody(self.__link3), odepy.dGeomGetBody(self.__manip))
        odepy.dJointSetFixed(self.__jointManip)

        # 目標値となるマニピュレータの位置
        self.__targetPos = [1, 1, 1]

        # IK を解いた結果の目標関節値と現在関節値の残差
        self.__eJointValues = [0.0, 0.0, 0.0]

        # 円軌道を描くための補助変数
        self.__phi = 0.0

    def GetTargetPos(self):
        return self.__targetPos

    def SetTargetPos(self, targetPos):
        self.__targetPos = targetPos

    def GetLinkLengthList(self):
        return self.__lBase, self.__l1, self.__l2, self.__l3, self.__lManip

    def MoveCircleTrajectory(self, x0=1.0, z0=1.2, r=0.5):
        self.__targetPos[0] = x0
        self.__targetPos[1] = r * np.sin(self.__phi)
        self.__targetPos[2] = r * np.cos(self.__phi) + z0
        self.__phi += 0.05

    def GetManipPos(self):
        # マニピュレータの位置を ODE の機能を利用して取得して返します。
        posOde = odepy.dGeomGetPosition(self.__manip)
        pos = np.zeros(3, dtype=np.float64)
        for i in range(len(pos)):
            pos[i] = posOde[i]
        return pos

    def Control(self, tDelta):
        jointValues = self.__SolveIk()
        kp = 10.0
        kd = 0.9
        fMax = 100.0
        for i, joint in enumerate([self.__joint1, self.__joint2, self.__joint3]):
            jointValue = odepy.dJointGetHingeAngle(joint)  # pi と -pi を越える際に不連続です。
            eJointValue = jointValues[i] - jointValue
            # jointValue が不連続であることに対応して以下の処理を行います。
            while eJointValue > np.pi:
                eJointValue -= 2.0 * np.pi
            while eJointValue < -np.pi:
                eJointValue += 2.0 * np.pi
            u = kp * eJointValue + kd * (eJointValue - self.__eJointValues[i]) / tDelta
            odepy.dJointSetHingeParam(joint, odepy.dParamVel, u)
            odepy.dJointSetHingeParam(joint, odepy.dParamFMax, fMax)
            self.__eJointValues[i] = eJointValue

    def __SolveIk(self):

        # 逆運動学を解析的に解いてジョイント値を取得します。
        px = self.__targetPos[0]
        py = self.__targetPos[1]
        pz = self.__targetPos[2]

        # 4つある解析解のひとつを利用します。
        tmpL = np.sqrt(px * px + py * py)
        p1p = np.sqrt(px * px + py * py + (pz - (self.__lBase + self.__l1)) * (pz - (self.__lBase + self.__l1)))
        ca = (self.__l2 * self.__l2 + p1p * p1p - (self.__l3 + self.__lManip / 2.0) * (self.__l3 + self.__lManip / 2.0)) / (2 * self.__l2 * p1p)
        phi = np.arctan2(pz - (self.__lBase + self.__l1), tmpL)
        alpha = np.arctan2(np.sqrt(1 - ca * ca), ca)
        cb = (self.__l2 * self.__l2 + (self.__l3 + self.__lManip / 2.0) * (self.__l3 + self.__lManip / 2.0) - p1p * p1p) / (2 * self.__l2 * (self.__l3 + self.__lManip / 2.0))
        beta = np.arctan2(np.sqrt(1 - cb * cb), cb)

        jointValues = np.zeros(3, dtype=np.float64)
        jointValues[0] = np.arctan2(py, -px)
        jointValues[1] = np.pi / 2.0 - phi - alpha
        jointValues[2] = np.pi - beta
        return jointValues

    def GetGeoms(self):
        return self.__base, self.__link1, self.__link2, self.__link3, self.__manip

    def __AddCylinder(self, world, space, r, l, m, px, py, pz, q, direction=3):
        geom = odepy.dCreateCylinder(space, r, l)
        body = odepy.dBodyCreate(world)
        mass = odepy.dMass()
        odepy.dMassSetZero(ctypes.byref(mass))
        odepy.dMassSetCylinderTotal(ctypes.byref(mass), m, direction, r, l)
        odepy.dGeomSetBody(geom, body)
        odepy.dBodySetMass(body, ctypes.byref(mass))
        odepy.dBodySetPosition(body, px, py, pz)
        odepy.dBodySetQuaternion(body, q)
        return geom

    def __AddCapsule(self, world, space, r, l, m, px, py, pz, q, direction=3):
        geom = odepy.dCreateCapsule(space, r, l)
        body = odepy.dBodyCreate(world)
        mass = odepy.dMass()
        odepy.dMassSetZero(ctypes.byref(mass))
        odepy.dMassSetCapsuleTotal(ctypes.byref(mass), m, direction, r, l)
        odepy.dGeomSetBody(geom, body)
        odepy.dBodySetMass(body, ctypes.byref(mass))
        odepy.dBodySetPosition(body, px, py, pz)
        odepy.dBodySetQuaternion(body, q)
        return geom

    def __AddJoint(self, world, body1, body2, pos, axis):
        joint = odepy.dJointCreateHinge(world, 0)
        odepy.dJointAttach(joint, body1, body2)
        odepy.dJointSetHingeAnchor(joint, *pos)
        odepy.dJointSetHingeAxis(joint, *axis)
        return joint

def RunDrawStuff(stepCallback, command, pathToTextures='/usr/local/share/ode-0.16.3-drawstuff-textures', w=400, h=225, cameraXyz=[3.0, 0.0, 1.0], cameraHpr=[-180.0, 0.0, 0.0]):
    def __StartCallback():
        xyz = (ctypes.c_float * 3)()
        hpr = (ctypes.c_float * 3)()
        for i, v in enumerate(cameraXyz):
            xyz[i] = v
        for i, v in enumerate(cameraHpr):
            hpr[i] = v
        ds.dsSetViewpoint(xyz, hpr)
    fn = ds.dsFunctions()
    fn.version = ds.DS_VERSION
    fn.start = ds.dsStartCallback(__StartCallback)
    fn.step = ds.dsStepCallback(stepCallback)
    fn.path_to_textures = ctypes.create_string_buffer(pathToTextures.encode('utf-8'))
    fn.command = ds.dsCommandCallback(command)
    ds.dsSimulationLoop(0, ctypes.byref(ctypes.POINTER(ctypes.c_char)()), w, h, fn)

def CreateWorld():
    odepy.dInitODE()
    world = odepy.dWorldCreate()
    odepy.dWorldSetGravity(world, 0.0, 0.0, -9.8)
    space = odepy.dHashSpaceCreate(0)
    ground = odepy.dCreatePlane(space, 0, 0, 1, 0)
    contactgroup = odepy.dJointGroupCreate(0)
    return world, space, ground, contactgroup

def DestroyWorld(world, space):
    odepy.dSpaceDestroy(space)
    odepy.dWorldDestroy(world)
    odepy.dCloseODE()

if __name__ == '__main__':
    Main()
