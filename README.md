# model-layer-profiling

## Docker

* build:

    ```
    $ docker build -f Dockerfile -t <image>:<tag> .
    ```

* run:

    * It is important to write ```--gpu all``` for exposing GPU information to docker container!

    ```
    $ docker run -it --gpus all <image>:<tag>
    ```

## Example

I porvide some examples how to use this tool to sumamrize layer information in Machine Learning Model. The all example under ```example``` folder and write shell script to automate install required Machine Learning model and do inference task, finally write layer information to file.

steps:
1. clone the repo
2. using ```dockerfile``` to build image and start up.
3. change directory to example you want, e.q. ```cd exmaple/tensorrt/resnet50``` to understand how to use the tool for Tensorrt engine.
4. every example has executable ```run.sh```, just run ```./run.sh``` you can see the result.


## Dependency

* nvidia-dlprof
    * [doc](https://docs.nvidia.com/deeplearning/frameworks/dlprof-user-guide/#using_ngc_docker_container)
    * [slide](https://tigress-web.princeton.edu/~jdh4/how_to_profile_with_dlprof_may_2021.pdf)
    * [dlprof user guide](https://docs.nvidia.com/deeplearning/frameworks/tensorboard-plugin-user-guide/index.html)
* TensorRT
    * [doc](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#python_topics)
* Pytorch
    * [doc](https://pytorch.org/get-started/locally/)
* nsys
    * [doc](https://docs.nvidia.com/nsight-systems/InstallationGuide/index.html)
