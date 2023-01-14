# Dockerfile for ODE
This is for building a ODE enviroment.

1. ## Build Image
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    To build the ROS-Foxy(default):
    ```bash:bash
    $ docker build -t my/ode:0.16.3 Dockerfile/simulation/ODE
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name ODE \
                 -v /tmp/.X11-unix:/tmp/.X11-unix \
                 -e DISPLAY=$DISPLAY \
                 -e QT_X11_NO_MITSHM=1 \
                 my/ode:0.16.3 /bin/bash
    ```
