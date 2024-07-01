#!/bin/bash

source /opt/ros/$ROS_DISTRO/setup.bash

mkdir -p /home/ros2_ws/src
cd /home/ros2_ws
colcon build --symlink-install

/bin/bash
