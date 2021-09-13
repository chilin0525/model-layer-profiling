# model-layer-profiling

## CLI command

We provide following function:
1. show GPU information: detect your GPU index and name, it is useful when you need choose a GPU to do inference task.
2. profile: summarize source used by every layer in Machine Learning model, e.q. duration, API call time, etc

usage: main.py [-h] [-c COMMAND] [-t {pytorch,tensorrt}] [-o OUTPUT_FILENAME] [-f {json,csv}] [-g GPU_IDX] [-l] function

### show GPU information

```TOOL_NAME gpuinfo```

### profile 

```TOOL_NAME profile -t <model_type>```

|short |long|possible parameters|default|description|
|:---|:---|:---|:---|:---|
|-t|--model_type|pytorch, tensorrt|-|choose model type|
|-o|--output|-|layer_inference_result| set summary file name|
|-f|--format|json,csv|write to file by simple format| set summary file format|
|-g|--gpu|-|0|set up gpu index to do inference|
|-l|--log|-|True|determine to delete log files or not,<br>if specific ```-l``` will keep log;<br>Otherwise, delete all log files|

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

I porvide some examples how to use this tool to sumamrize layer information in Machine Learning Model. The all example under ```example``` folder and exist shell script to automate install required Machine Learning model and do inference task, finally write layer information to file.

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
