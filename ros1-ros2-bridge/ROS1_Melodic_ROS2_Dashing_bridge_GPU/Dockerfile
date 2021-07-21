#### Install ROS1(melodic) & ROS2(dashing) on ubuntu18.04 ####
## docker build option: --build-arg ros1_ver=noetic ros2_ver=foxy

FROM nvidia/opengl:1.2-glvnd-runtime-ubuntu18.04

ARG ros1_ver=melodic 
ARG ros2_ver=dashing

ENV DEBIAN_FRONTEND=noninteractive


RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
    echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
    apt update && \
    apt install -y git tmux vim lsb-release curl gnupg2

### ROS1 Install ###
RUN apt update && \
    sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

ENV ROS1_DISTRO=$ros1_ver
RUN apt update && \
    apt install -y ros-$ROS1_DISTRO-desktop-full ros-$ROS1_DISTRO-turtlesim ros-$ROS1_DISTRO-rosserial ros-$ROS1_DISTRO-rosserial-arduino python-rosdep python-catkin-tools && \
    rosdep init && \
    rosdep update && \
    mkdir -p /home/ros1_ws/src && \
    cd /home/ros1_ws && \
    /bin/bash -c "source /opt/ros/$ROS1_DISTRO/setup.bash; catkin build"
    

### ROS2 Install ###
# 5 row execute zenntei
RUN apt update && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

ENV ROS2_DISTRO=$ros2_ver
RUN apt update && \
    apt install -y ros-$ROS2_DISTRO-desktop ros-$ROS2_DISTRO-ros1-bridge python3-colcon-common-extensions python3-argcomplete python3-vcstool python-rosdep && \
    mkdir -p /home/ros2_ws/src && \
    cd /home/ros2_ws && \
    /bin/bash -c "source /opt/ros/$ROS2_DISTRO/setup.bash; colcon build --symlink-install" && \
    apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "succesfully"
	
WORKDIR /home

    

### Before execute commands, following execute two comands###
## ROS1
#source /opt/ros/$ROS1_DISTRO/setup.bash
#source ~/catkin_ws/devel/setup.bash
## ROS2
#source /opt/ros/$ROS2_DISTRO/setup.bash
#source ~/ros2_ws/install/local_setup.bash && source ~/ros2_ws/install/setup.bash


### How to ROS1_BRIDGE ###
#https://gbiggs.github.io/rosjp_ros2_intro/ros1_bridge.html
#T1 = Terminal_1,T2 = Terminal_2, ...
#T1 # source /opt/ros/$ROS1_DISTRO/setup.bash
    # roscore
#T2 # source /opt/ros/$ROS2_DISTRO/setup.bash
    # source /opt/ros/$ROS1_DISTRO/setup.bash
    # export ROS_MASTER_URI=http://localhost:11311
    # ros2 run ros1_bridge dynamic_bridge --bridge-all-topics  //option[--bridge-all-topics]:トピックが利用されていなくても、ブリッジの反対側でtopic listに表示（どこかにデータが送信されているが、受信nodeがないこと）
#T3 # source /opt/ros/$ROS1_DISTRO/setup.bash
    # rosrun rospy_tutorials talker
#T4 # source /opt/ros/$ROS2_DISTRO/setup.bash
    # ros2 run demo_nodes_cpp listener


#RUN rm -rf /var/lib/apt/lists/*
