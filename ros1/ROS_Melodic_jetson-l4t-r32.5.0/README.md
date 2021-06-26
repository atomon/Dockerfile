# Dockerfile for ROS_Melodic_Jetson
This is for building a Jetson based ROS_Melodic enviroment. 
  
1. ## Build Image  
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    ROS-Melodic(on Jetson):
    ```bash:bash
    $ docker build -t my/ros:melodic_jetson-l4t-r32.5.0 Dockerfile/ros1/ROS_Melodic_jetson-l4t-r32.5.0
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name ROS_Melodic_5.0 \
                 --runtime nvidia \
                 --privileged \
                 --net=host \
                 -v /tmp/.X11-unix:/tmp/.X11-unix \
                 -e DISPLAY=$DISPLAY \
                 my/ros:melodic_jetson-l4t-r32.5.0 /bin/bash
    ```