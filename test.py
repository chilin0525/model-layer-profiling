from transformers import AutoTokenizer, AutoModel
import torch
import torch.cuda.profiler as profiler
import nvidia_dlprof_pytorch_nvtx


import torch.cuda.profiler as profiler
import pyprof
pyprof.init()
# nvidia_dlprof_pytorch_nvtx.init()
# torch.autograd.profiler.emit_nvtx()

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello world!", return_tensors="pt")
inputs.to("cuda:0")
# torch.save(model, "bert.pt")
model = torch.load("bert.pt")
model.to("cuda:0")
outputs = model(**inputs)
print(outputs)
