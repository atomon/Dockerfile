#### Install ROS1(melodic) & ROS2(dashing) on ubuntu18.04 ####
## docker build option: --build-arg ros1_ver=noetic ros2_ver=foxy

FROM ubuntu:18.04

ARG ros1_ver=melodic 
ARG ros2_ver=dashing

### ROS1 Install ###
RUN apt update && apt upgrade && \
    export ROS_DISTRO=ros1_ver && \
    apt install -y git tmux vim lsb-release curl gnupg2

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

RUN apt update && \
    apt install -y ros-$ROS_DISTRO-desktop-full ros-$ROS_DISTRO-turtlesim ros-$ROS_DISTRO-rosserial ros-$ROS_DISTRO-rosserial-arduino python-rosdep python-catkin-tools && \
    rosdep init && \
    rosdep update && \
    mkdir -p ~/catkin_ws/src && \
    cd ~/catkin_ws && \
    catkin build
    

### ROS2 Install ###
# 5 row execute zenntei
RUN apt update && \
    export ROS2_DISTRO=ros2_ver && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

RUN apt update && \
    apt install -y ros-$ROS2_DISTRO-desktop ros-$ROS2_DISTRO-ros-1bridge python3-colcon-common-extensions python3-argcomplete python3-vcstool && \
    mkdir -p ~/ros2_ws/src && \
    cd ~/ros_ws && \
    colcon build
    

### Before execute commands, following execute two comands###
## ROS1
#source /opt/ros/$ROS_DISTRO/setup.bash
#source ~/catkin_ws/devel/setup.bash
## ROS2
#source /opt/ros/$ROS2_DISTRO/setup.bash
#source ~/ros2_ws/install/local_setup.bash && source ~/ros2_ws/install/setup.bash


### How to ROS1_BRIDGE ###
#https://gbiggs.github.io/rosjp_ros2_intro/ros1_bridge.html
#T1 = Terminal_1,T2 = Terminal_2, ...
#T1 # source /opt/ros/$ROS_DISTRO/setup.bash
    # roscore
#T2 # source /opt/ros/$ROS2_DISTRO/setup.bash
    # source /opt/ros/$ROS_DISTRO/setup.bash
    # export ROS_MASTER_URI=http://localhost:11311
    # ros2 run ros1_bridge dynamic_bridge --bridge-all-topics  //option[--bridge-all-topics]:トピックが利用されていなくても、ブリッジの反対側でtopic listに表示（どこかにデータが送信されているが、受信nodeがないこと）
#T3 # source /opt/ros/$ROS_DISTRO/setup.bash
    # rosrun rospy_tutorials talker
#T4 # source /opt/ros/$ROS2_DISTRO/setup.bash
    # ros2 run demo_nodes_cpp listener


#RUN rm -rf /var/lib/apt/lists/*
