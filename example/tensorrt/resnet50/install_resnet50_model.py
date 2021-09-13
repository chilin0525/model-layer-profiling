import torch.onnx
import torchvision

BATCH_SIZE = 1
dummy_input = torch.randn(BATCH_SIZE, 3, 224, 224)

model = torchvision.models.resnet50(pretrained=True, progress=False).eval()
torch.onnx.export(model, dummy_input, "./resnet50.onnx",
                  verbose=False, input_names=['input'], output_names=['output'])
