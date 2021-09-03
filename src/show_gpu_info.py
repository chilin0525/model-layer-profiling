import torch

class gpu:
    def __init__(self,idx,name):
        self.idx = idx
        self.name = name

def show_gpu(verbose: bool):
    gpus = list()
    gpu_num = torch.cuda.device_count()
    for i in range(gpu_num):
        if(verbose):
            print(("gpu index: %d, gpu name: %s")%(i, torch.cuda.get_device_name(i)))
        gpus.append(gpu(i, torch.cuda.get_device_name(i)))
    return gpus
    
