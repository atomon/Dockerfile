#### Install ROS1(melodic) on ubuntu18.04 ####
## docker build option: --build-arg ros1_ver="noetic"
## docker run -it --name ROS_Melodic_GPU_Sim  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all my/ros-gpu:melodic /bin/bash


FROM nvidia/opengl:1.2-glvnd-runtime-ubuntu18.04

ARG ros1_ver=melodic
ENV ROS_DISTRO=$ros1_ver
ENV DEBIAN_FRONTEND=noninteractive

### ROS1 Install ###
RUN apt update && \
    apt install -y git tmux vim liburdfdom-tools lsb-release curl gnupg2

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

RUN apt update && \
    apt install -y ros-$ROS_DISTRO-desktop-full ros-$ROS_DISTRO-rosserial ros-$ROS_DISTRO-rosserial-arduino python-rosdep python-catkin-tools && \
    echo "ros installed" && \
    rosdep init && \
    rosdep update && \
    mkdir -p /home/ros1_ws/src && \
    cd /home/ros1_ws && \
    ls src && \
    /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash; catkin build" && \
    echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc && \
    echo "source /home/ros1_ws/devel/setup.bash" >> /root/.bashrc && \
    apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "succesfully"
	
WORKDIR /home/ros1_ws



### apt install package detail ###
# liburdfdom-tools //command{$ check_urdf [file_path]}:simple check for urdf_file

### apt available ros-package detail ###
# ros-melodic-joint-state-publisher-gui //for move arm(joint) on rviz 
# ros-melodic-turtlesim ros-melodic-effort-controllers ros-melodic-joint-trajectory-controller ros-melodic-joint-state-publisher-gui

### Before execute commands, following execute two comands###
## ROS1
#source /opt/ros/$ROS_DISTRO/setup.bash
#source ~/ros1_ws/devel/setup.bash

#RUN rm -rf /var/lib/apt/lists/*
