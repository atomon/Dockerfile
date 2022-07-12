FROM nvcr.io/nvidia/pytorch:21.08-py3

ENV DEBIAN_FRONTEND=noninteractive

RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
    echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
    apt update && \
    apt install -y fim zip htop screen libgl1-mesa-glx && \
    python -m pip install seaborn thop ruamel.yaml && \
	echo "succesfully"    

WORKDIR /home

