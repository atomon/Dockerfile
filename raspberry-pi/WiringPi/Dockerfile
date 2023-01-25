#######################################################################################################################################################################################
###  Install WiringPi on ubuntu20.04 for raspberry pi3 ###
#
## build
# $ docker build -t my/wiringpi:20.04 .
#
## run
# $ docker run -it --name WiringPi_GPIO -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all my/wiringpi:20.04 /bin/bash
#
#######################################################################################################################################################################################



FROM ubuntu:20.04


ENV DEBIAN_FRONTEND=noninteractive


##################################################
# set Bad proxy
# Install variable program
# Install Python & RPI.GPIO
# Install I2C
##################################################
RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
    echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
    apt update && \
    apt install -y git tmux vim liburdfdom-tools lsb-release curl gnupg2 fim make cmake gcc g++ && \
    apt install -y python3 python3-pip python3-rpi.gpio && \
    apt install -y i2c-tools python3-smbus


##################################################
# Create user
# Require sudo for wiringpi build
##################################################
ARG USERNAME=WiringPi_build
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
ARG PASSWORD=WiringPi_build
RUN apt update && apt install -y sudo && \
    echo "root:root" | chpasswd && \
    groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID -G sudo $USERNAME && \
    echo $USERNAME:$PASSWORD | chpasswd && \
    echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER WiringPi_build


##################################################
# Install WiringPi
# delete User(WiringPi_build)
##################################################
RUN cd /home/WiringPi_build && \
    git clone https://github.com/WiringPi/WiringPi.git && \
    cd /home/WiringPi_build/WiringPi && \
    ./build

USER root

RUN mv /home/WiringPi_build/WiringPi /home/ && \
    deluser --remove-home WiringPi_build && \
    rm /var/lib/apt/lists/lock && \
    rm /var/lib/dpkg/lock && \
    apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "succesfully"
	
WORKDIR /home/src



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


## docker build option: --build-arg ros1_ver=noetic and --build-arg ubuntu_ver=20.04
# $ docker build -t my/ros-gpu:noetic --build-arg ros1_ver=noetic --build-arg ubuntu_ver=20.04 .
