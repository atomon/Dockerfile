#######################################################################################################################################################################################
###  Install ROS2 on ubuntu ###
#
## build
# $ docker build -t my/ros-gpu:humble .
#
## docker build option: --build-arg ros1_ver=noetic and --build-arg ubuntu_ver=20.04
# $ docker build -t my/ros-gpu:dashing --build-arg ros2_ver=dashing --build-arg ubuntu_ver=18.04 .
#
## run
# $ docker run -it --name ROS_Foxy_GPU  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all my/ros-gpu:foxy /bin/bash
#
#######################################################################################################################################################################################



ARG ubuntu_ver=22.04

FROM nvidia/cuda:12.0.0-devel-ubuntu$ubuntu_ver


ENV TURTLEBOT3_MODEL=waffle
ENV DEBIAN_FRONTEND=noninteractive


#########################################
## Bad Proxy measures
## Set locale [UTF-8]
## Ubuntu Universe repository is enabled
#########################################
#RUN locale  ## check for UTF-8
RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
    echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
	apt update && apt install locales && \
	locale-gen en_US en_US.UTF-8  && \
	update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	apt -y install software-properties-common && \
	add-apt-repository universe
#RUN locale  ## verify settingsRUN apt update


#########################################
## Install variety
## Add the ROS2 GPG key with apt
## Add the repository to your sources list
#########################################
RUN apt update && apt install -y curl gnupg2 lsb-release tmux vim git wget locate python3-pip python3-flake8-docstrings && \
	updatedb && \
	curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null && \
	apt update && \
	apt upgrade
	

#########################################
## Install ROS2(Humble etc..) and turtlesim and teleop-twist-keyboard and Tool for ROS2
## setup workspace
## setup script の自動実行
#########################################
ARG ros2_ver=humble
ENV ROS_DISTRO=$ros2_ver
RUN apt install -y ros-$ROS_DISTRO-desktop ros-$ROS_DISTRO-turtlesim ros-humble-teleop-twist-keyboard ros-dev-tools && \
	python3 -m pip install -U argcomplete colcon-common-extensions vcstools && \
	echo "ros installed" && \
    rosdep init && \
    rosdep update && \
	mkdir -p /home/ros2_humble/src && cd /home/ros2_humble && \
	/bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash; colcon build --symlink-install" && \
	echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc && \
	echo "source /home/ros2_humble/install/setup.bash" >> ~/.bashrc && \
	echo "source /home/ros2_humble/install/local_setup.bash" >> ~/.bashrc


#########################################
## Install Gazebo Garden & Ignition
## Clean
#########################################
RUN apt update && \
	wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg && \
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null && \
	apt update && \
	apt -y install ignition-fortress ros-$ROS_DISTRO-ros-ign && \
	apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "succesfully"

WORKDIR /home/ros2_humble





#apt install ros-melodic-joint-state-publisher-gui
#vcs import src < turtlebot3.repos
#git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git && \
#git clone -b foxy https://github.com/ros2/examples && \


#docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all nvidia/opengl:1.2-glvnd-runtime-ubuntu20.04 /bin/bash

#RUN apt install -y python3 python3-pip vim
#RUN pip3 install torch torchvision jupyterlab matplotlib
#WORKDIR /work

#COPY train.py /work/

#ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
