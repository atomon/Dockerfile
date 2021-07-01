FROM nvidia/cuda:11.1-devel-ubuntu20.04

RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
    echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
    apt update && \
    apt install -y python3 python3-pip vim && \
    pip3 install torch torchvision jupyterlab matplotlib

WORKDIR /work

COPY train.py /work/

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
