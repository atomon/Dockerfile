#######################################################################################################################################################################################
# ros melodic ros-base 
#
# build
# $ docker build -t my/ros-jetson:melodic-l4t-r32.5.0 .
#
# run
# $ docker run -it --name ROS_Melodic_Study --runtime nvidia --privileged --net=host -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY my/ros-jetson:melodic-l4t-r32.5.0 /bin/bash
#
#######################################################################################################################################################################################

FROM nvcr.io/nvidia/l4t-base:r32.5.0

ARG ROS_PKG=desktop-full
ARG ros1_ver=melodic
ENV ROS_DISTRO=$ros1_ver
ENV DEBIAN_FRONTEND=noninteractive

# change the locale from POSIX to UTF-8
#RUN locale-gen en_US en_US.UTF-8 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
#ENV LANG=en_US.UTF-8

# add the ROS deb repo to the apt sources list
RUN apt update && \
    apt install -y git tmux vim software-properties-common build-essential cmake liburdfdom-tools lsb-release ca-certificates curl wget gnupg2

# add GPG-key and repository
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654


# install ROS packages
RUN apt update && \
    apt install -y ros-$ROS_DISTRO-${ROS_PKG} ros-$ROS_DISTRO-rosserial ros-$ROS_DISTRO-rosserial-arduino \
    python-rosdep python-rosinstall python-rosinstall-generator python-wstool python-catkin-tools python-vcstool  && \
    echo "ros installed" && \
    rosdep init && \
    rosdep update && \
    mkdir -p /home/ros1_ws/src && \
    cd /home/ros1_ws && \
    /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash; catkin build" && \
    echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc && \
    echo "source /home/ros1_ws/devel/setup.bash" >> /root/.bashrc && \
    apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "build succesfully"
	
WORKDIR /home/ros1_ws
