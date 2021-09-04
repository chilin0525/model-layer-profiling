import numpy as np
import torch
import torchvision
from PIL import Image
from matplotlib import pyplot as plt
from torchvision import transforms
import sys
import os
import torch.nn.functional as F
import torch.cuda.profiler as profiler
import pyprof

transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
      		std=[0.229, 0.224, 0.225])
])

def main():

    pyprof.init()

    model_name = "resnet50.pt"
    device = "cuda:0"

    img = Image.open('cat.png')
    img = transform(img)
    img = torch.unsqueeze(img, 0)
    img = img.to(device)

    gpu_model = torch.load(str(model_name))
    gpu_model.to(device)
    output = gpu_model(img)


if __name__ == "__main__":
    main()
