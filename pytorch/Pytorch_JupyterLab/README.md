# Dockerfile for Pytorch_JupyterLab
This is for building a Pytorch_JupyterLab enviroment. 
- CPU only
- Ubuntu 20.04
- Python3
- Jupyter Lab

1. ## Build Image  
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/cycling-Ohnishi/Dockerfile.git
    ```
    To build Pytorch enviroment:
    ```bash:bash
    $ docker build -t my/pytorch:py3-jupyterlab Dockerfile/pytorch/Pytorch_JupyterLab
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker run -it \
                 --name Pytorch_JupyterLab \
                 -p 8888:8888 \
                 my/pytorch:py3-jupyterlab /bin/bash
    ```
    To launch jupyter notebook server
    ```bash:bash
    $ jupyter lab --port 8888 --ip=* --allow-root
    ```
    Open the output URL in your host web browser.  
    ` http://127.0.0.1:8888/?token=...`

