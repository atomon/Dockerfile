# **Dockerfile manager**
These are for building a Docker enviroment.  
This version supports pytorch, ROS1 and ROS2 enviroment.  
ROS distribution supports Melodic, Dassing and Foxy.  
  
## **Build Image and RUN a Docker container based on image**
- ### **Pytorch**  
    |Tags|Detail|Link|doc|
    |:--|:--|:--:|:--:|
    |Pytorch|CPU only|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch/README.md)|
    |Pytorch_JupyterLab|CPU only<br>Include JupyterLab|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_JupyterLab)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_JupyterLab/README.md)|
    |Pytorch_GPU|Using Nvidia GPUs|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU/README.md)|
    |Pytorch_GPU_JupyterLab|Using Nvidia GPUs<br>Include JupyterLab|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU_JupyterLab)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/pytorch/Pytorch_GPU_JupyterLab/README.md)| 
- ### **ROS**
    |Type|Tags|Detail|Link|doc|
    |:--|:--|:--|:--:|:--:|
    |ROS1|melodic|CPU only|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic/README.md)|
    |ROS1|melodic_gpu|Using Nvidia GPUs|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_GPU)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_GPU/README.md)|
    |ROS1|melodic_jetson-l4t-r32.5.0|For Jetson|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_jetson-l4t-r32.5.0)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1/ROS_Melodic_jetson-l4t-r32.5.0/README.md)|
    |ROS2|xxx|CPU only<br>supports Dashing and Foxy|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros2/ROS2)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros2/ROS2/README.md)|
    |ROS2|xxx_gpu|Using Nvidia GPUs<br>supports Dashing and Foxy|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros2/ROS2_GPU)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros2/ROS2_GPU/README.md)|
    |1-2-Bridge|melodic-dashing|on ubuntu18.04|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1-ros2-bridge/ROS1_Melodic_ROS2_Dashing_bridge)|[●●●](https://github.com/cycling-Ohnishi/Dockerfile/tree/main/ros1-ros2-bridge/ROS1_Melodic_ROS2_Dashing_bridge/README.md)|
- ### **Simulation**
    |Type|Tags|Detail|Link|doc|
    |:--|:--|:--|:--:|:--:|
    |ODE|0.16.3|on ubuntu22.04|[●●●](https://github.com/atomon/Dockerfile/tree/main/simulation/ODE)|[●●●](https://github.com/atomon/Dockerfile/tree/main/simulation/ODE/README.md)|
- ### **RaspnerryPi**
    |Type|Tags|Detail|Link|doc|
    |:--|:--|:--|:--:|:--:|
    |WiringPi|latest|on ubuntu20.04|[●●●](https://github.com/atomon/Dockerfile/tree/main/raspberry-pi/WiringPi)|[●●●](https://github.com/atomon/Dockerfile/blob/main/raspberry-pi/WiringPi/README.md)|
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
