FROM ubuntu:20.04
# FROM python:3.8-alpine

RUN apt update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install python3.8
RUN apt -y install python3-pip

# Dlprof
RUN pip3 install nvidia-pyindex
RUN pip3 install nvidia-dlprof

# TensorRT
RUN pip3 install nvidia-tensorrt==7.2.3.* --index-url https://pypi.ngc.nvidia.com

# Pytorch
RUN pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

# gpustat
RUN pip3 install gpustat==0.6.0

# CMD pip3 list | grep nvidia