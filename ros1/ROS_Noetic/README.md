# Dockerfile for ROS_Noetic

This is for building a ROS_Noetic enviroment.

1. ## Build Image

   To clone the current relesse:

   ```bash:bash
   $ git clone https://github.com/atomon/Dockerfile.git
   ```

   ROS-Noetic:

   ```bash:bash
   $ docker build -t my/ros:noetic Dockerfile/ros1/ROS_Noetic
   ```

2. ## Run a Docker container based on image
   To run a docker container based on my/image:
   ```bash:bash
   $ docker run -it \
                --name ROS_Noetic \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                -e DISPLAY=$DISPLAY \
                -e QT_X11_NO_MITSHM=1 \
                my/ros:noetic /bin/bash
   ```
