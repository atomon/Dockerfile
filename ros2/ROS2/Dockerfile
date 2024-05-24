#######################################################################################################################################################################################
###  Install ROS2 on ubuntu ###
#
## build
# $ docker build -t my/ros:foxy .
#
## docker build option: --build-arg ros1_ver=noetic and --build-arg ubuntu_ver=20.04
# $ docker build -t my/ros:dashing --build-arg ros2_ver=dashing --build-arg ubuntu_ver=18.04 .
#
## run
# $ docker run -it --name ROS_Foxy  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 my/ros:foxy /bin/bash
#
#######################################################################################################################################################################################



ARG base_image=ubuntu:22.04
FROM $base_image


ENV TURTLEBOT3_MODEL=waffle
ENV DEBIAN_FRONTEND=noninteractive


# RUN locale  ## check for UTF-8  https://hub.docker.com/r/nvidia/opengl
# RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
# 	echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy
RUN apt update && apt install locales && \
	locale-gen en_US en_US.UTF-8  && \
	update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
	export LANG=en_US.UTF-8
# RUN locale  ## verify settingsRUN apt update

RUN apt update && apt install -y curl gnupg2 lsb-release tmux vim git wget python3-pip && \
	curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null && \
	apt update && apt upgrade -y


ARG ros2_ver=humble
ENV ROS_DISTRO=$ros2_ver

#Indtall ROS2(Foxy etc..) and Install Tool for ROS2 and setup script の自動実行 and Install turtlesim and gazebo and Install ros2_example and turtulebot3_gazebo(waffle or burger)
RUN apt install -y ros-$ROS_DISTRO-desktop ros-$ROS_DISTRO-turtlesim ros-$ROS_DISTRO-gazebo-ros-pkgs \
	python3-rosdep python3-argcomplete python3-colcon-common-extensions && \
	echo "ros installed" && \
	rosdep init && \
	rosdep update && \
	echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc && \
	echo "source /home/ros2_ws/install/setup.bash" >> ~/.bashrc && \
	echo "source /home/ros2_ws/install/local_setup.bash" >> ~/.bashrc && \
	rm -rf /var/lib/apt/lists/* && \
	echo "succesfully"

WORKDIR /home/ros2_ws

COPY ./entrypoint.sh /tmp/entrypoint.sh
RUN chmod 755 /tmp/entrypoint.sh
ENTRYPOINT [ "/tmp/entrypoint.sh" ]


#apt install ros-melodic-joint-state-publisher-gui
#vcs import src < turtlebot3.repos
#git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git && \
#git clone -b foxy https://github.com/ros2/examples && \


#docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all nvidia/opengl:1.2-glvnd-runtime-ubuntu20.04 /bin/bash
#ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
