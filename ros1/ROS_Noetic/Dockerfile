#######################################################################################################################################################################################
###  Install ROS1(melodic) on ubuntu18.04 ###
#
## build
# $ docker build -t my/ros-gpu:melodic .
#
## run
# $ docker run -it --name ROS_Melodic_GPU  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all my/ros-gpu:melodic /bin/bash
#
#######################################################################################################################################################################################


ARG ubuntu_ver=20.04
ARG base_image=ubuntu:$ubuntu_ver

FROM $base_image


ENV DEBIAN_FRONTEND=noninteractive

### ROS1 Install ###
# RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
#     echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
RUN apt update && apt upgrade -y && \
    apt install -y git tmux vim liburdfdom-tools lsb-release curl gnupg2 net-tools wget curl locate

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

ARG ros1_ver=noetic
ENV ROS_DISTRO=$ros1_ver

RUN apt update && \
    apt install -y ros-$ROS_DISTRO-desktop-full ros-$ROS_DISTRO-rosserial ros-$ROS_DISTRO-rosserial-arduino \
    python3-rosdep python3-catkin-tools python3-rospkg && \
    echo "ros installed" && \
    rosdep init && \
    rosdep update && \
    echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc && \
    echo "source /home/ros1_ws/devel/setup.bash" >> ~/.bashrc && \
    apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "succesfully"

WORKDIR /home/ros1_ws

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]


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
