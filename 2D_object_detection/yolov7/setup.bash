#!/bin/bash

mkdir weights
mkdir datasets

git clone https://github.com/WongKinYiu/yolov7.git

cd weights
curl -OL https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
curl -OL https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt
