#Dockerfile manager
---
These are for building a Docker enviroment.  
This version supports pytorch, ROS1 and ROS2 enviroment.  
ROS distribution supports Melodic, Dassing and Foxy.  
  
## Build Image  
### Ubuntu
To clone the current relesse:
```bash:bash
$ git clone https://
```
####pytorch:
```bash:bash
$ docker build -t my/pytorch:latest Dockerfile/pytorch/pytorch/.
```
or
####ros-melodic(Using Nvidia GPU):
```bash:bash
$ docker build -t my/ros-gpu:melodic Dockerfile/ros1/ROS_Melodic_GPU
```
or
####ros-melodic(Using jetson):
``` bash:bash
$ docker build -t my/ros-jetson:melodic Dockerfile/ros1/ROS_Melodic_jetson-l4t-r32.5.0
```
or
####ros-foxy(Using Nvidia GPU):
```bash:bash
$ docker build -t my/ros-gpu:foxy Dockerfile/ros2/ROS_Foxy_GPU
```

```c:test
int a=0;
#include g.h
```


##Run a Docker container based on image
###Ubuntu
To run a docker container based on my/image:
```bash:bash
$ docker run 
```

##Stop runed container
###Ubuntu
To stop runed container:
```bash:bash
$ docker stop 
```

##Start one or more stopped container
###Ubuntu
```bash:bash
$ docker start
```

##Run command
