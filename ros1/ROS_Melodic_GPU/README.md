# Dockerfile for ROS_Melodic_GPUs

This is for building a GPUs based ROS_Melodic enviroment.

1. ## Build Image

   To clone the current relesse:

   ```bash:bash
   $ git clone https://github.com/atomon/Dockerfile.git
   ```

   ROS-Melodic(Using Nvidia GPUs):

   ```bash:bash
   $ docker build -t my/ros:gpu-melodic Dockerfile/ros1/ROS_Melodic_GPU
   ```

2. ## Run a Docker container based on image
   To run a docker container based on my/image:
   ```bash:bash
   $ docker run -it \
                --name ROS_Melodic_GPU \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                -e DISPLAY=$DISPLAY \
                -e QT_X11_NO_MITSHM=1 \
                --gpus all \
                my/ros:gpu-melodic /bin/bash
   ```
