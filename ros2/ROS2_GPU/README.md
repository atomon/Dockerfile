# Dockerfile for ROS2_GPUs

This is for building a GPUs based ROS2 enviroment.  
ROS2 distribution supports Dashing and Foxy.

1. ## Build Image

   To clone the current relesse:

   ```bash:bash
   $ git clone https://github.com/atomon/Dockerfile.git
   ```

   To build the ROS-Humble(default):

   ```bash:bash
   $ docker build -t my/ros:gpu-humble Dockerfile/ros2/ROS2_GPU
   ```

   &nbsp;&nbsp;or  
   To build the ROS-foxy(option):

   ```bash:bash
   $ docker build -t my/ros:gpu-foxy \
                  --build-arg base_image=nvidia/opengl:1.2-glvnd-runtime-ubuntu20.04
   ```

2. ## Run a Docker container based on image
   To run a docker container based on my/image:
   ```bash:bash
   $ docker run -it \
                --name ROS_Humble_GPU \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                -e DISPLAY=$DISPLAY \
                -e QT_X11_NO_MITSHM=1 \
                --gpus all \
                my/ros:gpu-humble /bin/bash
   ```
   &nbsp;&nbsp;or  
   To run a docker container based on my/image(in the case of Foxy):
   ```bash:bash
   $ docker run -it \
                --name ROS_Foxy_GPU \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                -e DISPLAY=$DISPLAY \
                -e QT_X11_NO_MITSHM=1 \
                --gpus all \
                my/ros:gpu-foxy /bin/bash
   ```
