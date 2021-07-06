# Dockerfile for Pytorch
This is for building a Pytorch enviroment. 
- CPU only
- Ubuntu 20.04
- Python3  

1. ## Build Image  
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    To build Pytorch enviroment:
    ```bash:bash
    $ docker build -t my/pytorch:py3 Dockerfile/pytorch/Pytorch
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name Pytorch \
                 --gpus all \
                 my/pytorch:py3 /bin/bash
    ```