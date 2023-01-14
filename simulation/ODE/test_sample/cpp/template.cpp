#include <ode/ode.h>                // ODE用ヘッダーファイル
#include <drawstuff/drawstuff.h>    // 描画用ヘッダーファイル

#include "template.h"

void simLoop(int pause)           /***  シミュレーションループ　***/
{
  dWorldStep(world,0.01);        // シミュレーションを1ステップ進める

  dsSetColor(1.0,0.0,0.0);                     // 赤色の設定(r,g,b)
  const dReal *pos = dBodyGetPosition(apple);  // リンゴの位置を取得
  const dReal *R   = dBodyGetRotation(apple);  // リンゴの姿勢を取得
  dsDrawSphereD(pos,R,r);                      // リンゴの描画
}

void start()                                  /*** 前処理　***/
{
  static float xyz[3] = {3.0,0.0,1.0};         // 視点の位置
  static float hpr[3] = {-180, 0, 0};          // 視線の方向
  dsSetViewpoint(xyz,hpr);                     // カメラの設定
}

void setDrawStuff()           /*** 描画関数の設定 ***/
{
  fn.version = DS_VERSION;    // ドロースタッフのバージョン
  fn.start   = &start;        // 前処理 start関数のポインタ
  fn.step    = &simLoop;      // simLoop関数のポインタ
  fn.path_to_textures = "/home/libode/ode-0.16.3/drawstuff/textures"; // テクスチャ
}

int main(int argc, char **argv)         /*** main関数 ***/
{
  setDrawStuff();                          // 描画関数の設定

  dInitODE2(0);                            // 初期化
  world = dWorldCreate();                  // 世界の創造
  dWorldSetGravity(world,0,0,-0.2);        // 重力設定

  apple = dBodyCreate(world);              // ボールの生成
  dMass mass;                              // 構造体massの宣言
  dMassSetZero(&mass);                     // 構造体massの初期化
  dMassSetSphereTotal(&mass,m,r);          // 構造体massに質量を設定
  dBodySetMass(apple,&mass);               // ボールにmassを設定
  dBodySetPosition(apple, 0.0, 0.0, 2.0);  // ボールの位置(x,y,z)を設定

  dsSimulationLoop(argc,argv,640, 480,&fn); // シミュレーションループ
  dWorldDestroy(world);                     // 世界の終焉
  dCloseODE();
  return 0;
}
