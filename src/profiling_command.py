def generate_command(model_type, gpu_idx, command):

    dlprof = "dlprof --reports all" + \
                      " --force=true" + \
                      " --mode=" + model_type + \
                      " --formats=json" + \
                      " --output_path=log " + command
    
    return dlprof
