#
#  docker run -it --privileged --gpus all --name opencvs -e NVIDIA_DRIVER_CAPABILITIES=all -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 nvidia/cuda:11.0-devel-ubuntu18.04 /bin/bash
#

FROM nvidia/cuda:11.0-devel-ubuntu18.04

#ENV NVIDIA_DRIVER_CAPABILITIES all

RUN apt update && \
    apt purge *libopencv* && \
    apt install -y --no-install-recommends \
    build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
    libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev \
    libv4l-dev v4l-utils qv4l2 v4l2ucp \
    unzip curl git vim && \
    rm -rf /var/lib/apt/lists/*

# Install OpenCV with CUDA
RUN version="4.5.0" && \
    folder="workspace" && \
    echo "** Download opencv-"${version} \
    mkdir $folder && cd ${folder} && \
    curl -L https://github.com/opencv/opencv/archive/${version}.zip -o opencv-${version}.zip && \
    curl -L https://github.com/opencv/opencv_contrib/archive/${version}.zip -o opencv_contrib-${version}.zip && \
    unzip opencv-${version}.zip && \
    unzip opencv_contrib-${version}.zip && \
    cd opencv-${version} && \
    mkdir build && cd build/ && \
    cmake -D WITH_CUDA=ON \
	  -D WITH_CUDNN=ON \
	  -D CUDA_ARCH_BIN="5.3,6.1,7.2" \
  	  -D CUDA_ARCH_PTX="" \
	  -D OPENCV_GENERATE_PKGCONFIG=ON \
	  -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-${version}/modules \
	  -D WITH_GSTREAMER=ON \
	  -D WITH_LIBV4L=ON \
	  -D BUILD_opencv_python2=ON \
	  -D BUILD_opencv_python3=ON \
	  -D BUILD_TESTS=OFF \
	  -D BUILD_PERF_TESTS=OFF \
	  -D BUILD_EXAMPLES=OFF \
	  -D CMAKE_BUILD_TYPE=RELEASE \
	  -D CMAKE_INSTALL_PREFIX=/usr/local .. && \
    make -j5 && \
    make install && \
    pkg-config --modversion opencv4

RUN cd /home && \
    git clone https://github.com/niconielsen32/ComputerVision.git && \
    cd ComputerVision/OpenCVGPU/ && \
    mkdir build && cd build/ && \
    cmake .. && make && \
    ./opencvGPUtestyoutube
