# Dockerfile for Pytorch_GPU
This is for building a GPUs based Pytorch enviroment. 
- CUDA 11.1
- Ubuntu 20.04 (GPU)
- Python3  

1. ## Build Image  
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    To build Pytorch_GPU enviroment:
    ```bash:bash
    $ docker build -t my/pytorch:gpu-py3 Dockerfile/pytorch/Pytorch_GPU
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name Pytorch_GPU \
                 --gpus all \
                 my/pytorch:gpu-py3 /bin/bash
    ```