#!/bin/bash

source /opt/ros/$ROS_DISTRO/setup.bash

mkdir -p /home/ros1_ws/src
cd /home/ros1_ws
catkin build

/bin/bash
