FROM nvidia/opengl:1.2-glvnd-runtime-ubuntu20.04

ARG ros2_ver=foxy
ENV ROS_DISTRO=$ros2_ver
ENV TURTLEBOT3_MODEL=waffle
ENV DEBIAN_FRONTEND=noninteractive


#RUN locale  ## check for UTF-8  https://hub.docker.com/r/nvidia/opengl
RUN apt update && apt install locales && \
	locale-gen en_US en_US.UTF-8  && \
	update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
	export LANG=en_US.UTF-8
#RUN locale  ## verify settingsRUN apt update

RUN apt update && apt install -y curl gnupg2 lsb-release tmux vim git wget python3-pip python3-vcstools&& \
	curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
	sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list' && \
	apt update

#Indtall ROS2(Foxy etc..) and Install Tool for ROS2 and setup script の自動実行 and Install turtlesim and gazebo and Install ros2_example and turtulebot3_gazebo(waffle or burger)
RUN apt install -y ros-$ROS_DISTRO-desktop && \
	apt install -y python3-argcomplete python3-colcon-common-extensions ros-$ROS_DISTRO-turtlesim ros-$ROS_DISTRO-gazebo-ros-pkgs && \
	source /opt/ros/$ROS_DISTRO/setup.bash && \
	echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc && \
	mkdir -p /home/ros2_ws && cd /home/ros2_ws && \
	colcon build --symlink-install && \
	source /home/ros2_ws/install/setup.bash && \
	source /home/ros2_ws/install/local_setup.bash && \
	echo "source /home/ros2_ws/install/setup.bash" >> ~/.bashrc && \
	echo "source /home/ros2_ws/install/local_setup.bash" >> ~/.bashrc && \
	mkdir -p /home/ros2_ws/src/myProjects && cd src && \
	git clone -b foxy https://github.com/ros2/examples && \
	cd .. && colcon build
	
#apt install ros-melodic-joint-state-publisher-gui
#vcs import src < turtlebot3.repos
#git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git && \




#docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all nvidia/opengl:1.2-glvnd-runtime-ubuntu20.04 /bin/bash

#RUN apt install -y python3 python3-pip vim
#RUN pip3 install torch torchvision jupyterlab matplotlib
#WORKDIR /work

#COPY train.py /work/

#ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
