# Dockerfile for ROS1_ROS2_Bridge
This is for building a ROS1_ROS2_Bridge enviroment.  
ROS distribution supports Dashing and Melodic.

1. ## Build Image
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    To build the ROS_Bridge enviroment:
    ```bash:bash
    $ docker build -t my/ros-bridge:melodic-dashing Dockerfile/ros1-ros2-bridge/ROS1_Melodic_ROS2_Dashing_bridge
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name ROS1_Melodic_ROS2_Dashing_bridge \
                 -v /tmp/.X11-unix:/tmp/.X11-unix \
                 -e DISPLAY=$DISPLAY \
                 -e QT_X11_NO_MITSHM=1 \
                 my/ros-bridge:melodic-dashing /bin/bash
    ```