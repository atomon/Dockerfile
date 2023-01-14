#######################################################################################################################################################################################
###  Install Open Dynamics Engine(ODE) on ubuntu ###
## Sorce URL: 
#			  https://bitbucket.org/odedevs/ode/src/master/
#			  https://github.com/qoosky/ode-python/tree/master/odepy
#
## ref URL:
#          	https://demura.net/tutorials
#          	https://www.qoosky.io/techs/4549728ae8
#		   	https://stackoverflow.com/questions/28481900/oserror-cannot-open-shared-object-file-no-such-file-or-directory-even-though-f
#
## build
# $ docker build -t my/ode:0.16.3 .
#
## docker build option: --build-arg ros1_ver=noetic and --build-arg ubuntu_ver=20.04
# $ docker build -t my/ros-gpu:dashing --build-arg ros2_ver=dashing --build-arg ubuntu_ver=18.04 .
#
## run
# $ docker run -it --name ODE  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all my/ode:0.16.3 /bin/bash
#
#######################################################################################################################################################################################



ARG ubuntu_ver=22.04

FROM ubuntu:$ubuntu_ver


ENV DEBIAN_FRONTEND=noninteractive
ENV LD_LIBRARY_PATH=/usr/local/lib


#########################################
## Bad Proxy measures
#########################################
RUN touch /etc/apt/apt.conf.d/99fixbadproxy && \
    echo "Acquire::http::Pipeline-Depth 0; Acquire::http::No-Cache true; Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99fixbadproxy


#########################################
## Install variety
#########################################
RUN apt update && apt install -y curl gnupg2 lsb-release tmux vim git wget locate python3 python3-pip python3-flake8-docstrings && \
	updatedb
	

#########################################
## Install ODE
#########################################
RUN mkdir -p /home/libode && cd /home/libode && \ 
	curl -OL https://bitbucket.org/odedevs/ode/downloads/ode-0.16.3.tar.gz && \
	tar zxvf ode-0.16.3.tar.gz && \
	cd ode-0.16.3 && \
	./configure --enable-double-precision && \
	make &&\
	echo "Installed ODE"


#########################################
## Install ODE python_ver
#########################################
RUN apt update && \
	apt install -y libgl1-mesa-dev libglu1-mesa-dev cmake && \
	python3 -m pip install -U argcomplete matplotlib numpy scipy ode-python && \
	mkdir -p /home/libode/ode-0.16.3/mybuild && cd /home/libode/ode-0.16.3/mybuild && \
	cmake ../ -DBUILD_SHARED_LIBS=ON -DODE_WITH_DEMOS=ON && \
	make && \
	cp libdrawstuff.so /usr/local/lib/ && \
	cp -d libode.so.0.16.3 libode.so /usr/local/lib/ && \
	cp -r ../drawstuff/textures /usr/local/share/ode-0.16.3-drawstuff-textures && \
	chmod -R a+x /usr/local/share/ode-0.16.3-drawstuff-textures && \
	apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "succesfully"

COPY test_sample /home/test_sample
WORKDIR /home/





#apt install ros-melodic-joint-state-publisher-gui
#vcs import src < turtlebot3.repos
#git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git && \
#git clone -b foxy https://github.com/ros2/examples && \


#docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --gpus all nvidia/opengl:1.2-glvnd-runtime-ubuntu20.04 /bin/bash

#RUN apt install -y python3 python3-pip vim
#RUN pip3 install torch torchvision jupyterlab matplotlib
#WORKDIR /work

#COPY train.py /work/

#ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
