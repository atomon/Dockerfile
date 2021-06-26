FROM nvidia/cuda:11.1-devel-ubuntu20.04

RUN apt update
RUN apt install -y python3 python3-pip vim
RUN pip3 install torch torchvision jupyterlab matplotlib

WORKDIR /work

COPY train.py /work/

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
