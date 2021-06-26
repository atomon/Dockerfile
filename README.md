# **Dockerfile manager**
These are for building a Docker enviroment.  
This version supports pytorch, ROS1 and ROS2 enviroment.  
ROS distribution supports Melodic, Dassing and Foxy.  
  
## **Build Image and RUN a Docker container based on image**
- ### **Pytorch**  
    |Tags|Detail|Link|doc|
    |:--|:--|:--:|:--:|
    |Pytorch_GPU|Using Nvidia GPUs|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU/README,md)|
    |Pytorch_GPU_JupyterLab|Include JupyterLab|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU_JupyterLab)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU_JupyterLab/README.md)| 
- ### **ROS1**
    |Tags|Detail|Link|doc|
    |:--|:--|:--:|:--:|
    |melodic_gpu|Using Nvidia GPUs|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_GPU)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_GPU/README.md)|
    |melodic_jetson-l4t-r32.5.0|For Jetson|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_jetson-l4t-r32.5.0)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_jetson-l4t-r32.5.0/README.md)|
- ### **ROS2**
    |Tags|Detail|Link|doc|
    |:--|:--|:--:|:--:|
    |xxx_gpu|supports Dashing and Foxy<br>Using Nvidia GPUs|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros2/ROS2_GPU)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros2/ROS2_GPU/README.md)|
- ### **ROS1-ROS2-Bridge**
    |Tags|Detail|Link|doc|
    |:--|:--|:--:|:--:|
    |melodic-dashing|on ubuntu18.04|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1-ros2-bridge/ROS1_Melodic_ROS2_Dashing_bridge)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1-ros2-bridge/ROS1_Melodic_ROS2_Dashing_bridge/README.md)|
<br>
<br>

## **Docker Command Reference**
1. ### **Stop runed container**
    To stop runed container:
    ```bash:bash
    $ docker stop ROS_Melodic_GPU
    ```

2. ### **Start one or more stopped container**
    ```bash:bash
    $ docker start [OPTIONS] CONTAINER_NAME [CONTAINER_NAME...]
    ```
    e.g.
    ```bash:bash
    $ docker start ROS_Melodic_GPU
    ```

3. ### **Launch command line**
    ```bash:bash
    $ docker exec [OPTIONS] CONTAINER_NAME COMMAND [ARG...]
    ```
    e.g.
    ```bash:bash
    $ docker exec -it ROS_Melodic_GPU /bin/bash
    ```
<br>
<br>

>ref:  
https://docs.docker.com/reference/