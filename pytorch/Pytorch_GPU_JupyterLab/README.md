# Dockerfile for Pytorch_GPU_JupyterLab
This is for building a GPUs based Pytorch_JupyterLab enviroment. 
- CUDA 11.1
- Ubuntu 20.04 (GPU)
- Python3
- Jupyter Lab

1. ## Build Image  
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    To build Pytorch_GPU enviroment:
    ```bash:bash
    $ docker build -t my/pytorch:gpu-py3-jupyterlab Dockerfile/pytorch/Pytorch_GPU_JupyterLab
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name Pytorch_GPU_JupyterLab \
                 -p 8888:8888 \
                 --gpus all \
                 my/pytorch:gpu-py3-jupyterlab /bin/bash
    ```
    To launch jupyter notebook server
    ```bash:bash
    $ jupyter lab --port 8892 --ip=* --allow-root
    ```
    Open the output URL in your host web browser.  
    ` http://127.0.0.1:8888/?token=...`

