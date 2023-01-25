# Dockerfile for WiringPi on Raspberry Pi
This is for building a WiringPi enviroment. 

1. ## Using Docker-Compose
    1. Build & Run
        ```
        $ git clone https://github.com/atomon/Dockerfile.git
        $ cd Dockerfile/raspberry=pi/WiringPi/
        $ docker-compose up --build -d
        $ docker-compose exec WiringPi bash
        ```

1. ## Not Using Docker-Compose
    1. ### Build Image
        To clone the current relesse:
        ```bash:bash
        $ git clone https://github.com/atomon/Dockerfile.git
        ```
        Build:
        ```bash:bash
        $ docker build -t my/wiringpi:latest Dockerfile/raspberry=pi/WiringPi/
        ```

    2. ### Run a Docker container based on image
        To run a docker container based on my/image:
        ```bash:bash
        $ docker run -it \
                     --name WiringPi \
                     --privileged \
                     -v /tmp/.X11-unix:/tmp/.X11-unix \
                     -e DISPLAY=$DISPLAY \
                     -e QT_X11_NO_MITSHM=1 \
                     my/wiringpi:latest /bin/bash 
        ```