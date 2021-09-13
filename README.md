# model-layer-profiling

* dependency
    * nvidia-dlprof
        * [doc](https://docs.nvidia.com/deeplearning/frameworks/dlprof-user-guide/#using_ngc_docker_container)
        * [slide](https://tigress-web.princeton.edu/~jdh4/how_to_profile_with_dlprof_may_2021.pdf)
        * [dlprof user guide](https://docs.nvidia.com/deeplearning/frameworks/tensorboard-plugin-user-guide/index.html)
    * TensorRT
        * [doc](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#python_topics)
    * Pytorch
        * [doc](https://pytorch.org/get-started/locally/)

## Docker

* build:

    ```
    $ docker build -f Dockerfile -t <image>:<tag> .
    ```

* run:

    ```
    $ docker run -it --gp
    ```