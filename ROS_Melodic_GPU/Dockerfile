#### Install ROS1(melodic) & ROS2(dashing) on ubuntu18.04 ####
## docker build option: --build-arg ros1_ver="noetic"


FROM nvidia/opengl:1.2-glvnd-runtime-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
ARG ros1_ver=melodic
ENV ROS_DISTRO=$ros1_ver
WORKDIR /home/ros1_ws

### ROS1 Install ###
RUN apt update && \
    echo $ROS_DISTRO && \
    apt install -y git tmux vim liburdfdom-tools lsb-release curl gnupg2

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

RUN apt update && \
    apt install -y ros-melodic-desktop-full ros-melodic-turtlesim ros-melodic-effort-controllers ros-melodic-joint-trajectory-controller ros-melodic-joint-state-publisher-gui ros-melodic-rosserial ros-melodic-rosserial-arduino python-rosdep python-catkin-tools && \
    source /opt/ros/melodic/setup.bash && \
    rosdep init && \
    rosdep update && \
    mkdir -p /home/ros1_ws/src && \
    cd /home/ros1_ws && \
    catkin build && \
    echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc && \
    echo "source /home/ros1_ws/devel/setup.bash" >> ~/.bashrc && \
    apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
	


### apt install package detail ###
# liburdfdom-tools //command{$ check_urdf [file_path]}:simple check for urdf_file

### apt install ros-package detail ###
# ros-melodic-joint-state-publisher-gui //for move arm(joint) on rviz 

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
