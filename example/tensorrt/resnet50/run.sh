# install pytorch  resnet50 pretrained model and export to ONNX format, 
# save as resnet50.onnx
python3 install_resnet50_model.py

# build engine from resnet50.onnx and save engine to resnet50.plan
python3 onnx2trt.py

# do infernece task and use our tool to trace the detail of GPU resource and duration
python3 ../../../src/main.py -c "python3 trt_profiler.py 0" -t tensorrt