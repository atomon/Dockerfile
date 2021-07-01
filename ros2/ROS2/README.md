# Dockerfile for ROS2
This is for building a ROS2 enviroment.  
ROS2 distribution supports Dashing and Foxy.

1. ## Build Image
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    To build the ROS-Foxy(default):
    ```bash:bash
    $ docker build -t my/ros:foxy Dockerfile/ros2/ROS2
    ```
    &nbsp;&nbsp;or  
    To build the ROS-dashing(option):
    ```bash:bash
    $ docker build -t my/ros:dashing \
                   --build-arg ros2_ver=dashing \
                   --build-arg ubuntu_ver=18.04 Dockerfile/ros2/ROS2
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name ROS_Foxy \
                 -v /tmp/.X11-unix:/tmp/.X11-unix \
                 -e DISPLAY=$DISPLAY \
                 -e QT_X11_NO_MITSHM=1 \
                 my/ros:foxy /bin/bash
    ```
    To run a docker container based on my/image(in the case of Dashing):
    ```bash:bash
    $ docker run -it \
                 --name ROS_Dashing \
                 -v /tmp/.X11-unix:/tmp/.X11-unix \
                 -e DISPLAY=$DISPLAY \
                 -e QT_X11_NO_MITSHM=1 \
                 my/ros:dashing /bin/bash
    ```