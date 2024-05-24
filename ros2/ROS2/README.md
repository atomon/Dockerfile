# Dockerfile for ROS2

This is for building a ROS2 enviroment.  
ROS2 distribution supports Humble or later.

1. ## Build Image

   To clone the current relesse:

   ```bash:bash
   $ git clone https://github.com/atomon/Dockerfile.git
   ```

   To build the ROS-Humble(default):

   ```bash:bash
   $ docker build -t my/ros:humble Dockerfile/ros2/ROS2
   ```

   &nbsp;&nbsp;or  
   To build the ROS-dashing(option):

   ```bash:bash
   $ docker build -t my/ros:foxy \
                  --build-arg ros2_ver=foxy \
                  --build-arg ubuntu_ver=18.04 Dockerfile/ros2/ROS2
   ```

2. ## Run a Docker container based on image
   To run a docker container based on my/image:
   ```bash:bash
   $ docker run -it \
                --name ROS_Humble \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                -e DISPLAY=$DISPLAY \
                -e QT_X11_NO_MITSHM=1 \
                my/ros:humble /bin/bash
   ```
   &nbsp;&nbsp;or  
   To run a docker container based on my/image(in the case of Dashing):
   ```bash:bash
   $ docker run -it \
                --name ROS_Humble \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                -e DISPLAY=$DISPLAY \
                -e QT_X11_NO_MITSHM=1 \
                my/ros:humble /bin/bash
   ```
