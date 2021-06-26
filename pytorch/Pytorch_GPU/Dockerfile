FROM nvidia/cuda:11.1-devel-ubuntu20.04

RUN apt update && \
    apt install -y python3 python3-pip && \
    pip3 install torch torchvision matplotlib

WORKDIR /work

COPY train.py /work/

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
