def generate_command(model_type, model_path, gpu_idx):
    

    if(model_type=="pytorch"):
        profiler = "pytorch_profiler"
    elif(model_type=="onnx"):
        profiler = "onnx_profiler"
    elif(model_type=="tensorrt"):
        profiler = "tensorrt_profiler"

    profiler += ".py"
    dlprof = "dlprof --reports all" + \
                      " --force=true" + \
                      " --mode=" + model_type + \
                      " --formats=json" + \
                      " --output_path=log python3 ./src/" + profiler

    dlprof += " " + model_path
    dlprof += " " + gpu_idx
    
    return dlprof
