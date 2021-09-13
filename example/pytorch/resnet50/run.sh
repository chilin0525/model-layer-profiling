# install pytorch pretrained model and save as resnet50.pt
python3 install_resnet50_model.py 

# using our tool to do inference and summary GPU information for every layer in model
python3 ../../../src/main.py -c "python3 pytorch_profiler.py resnet50.pt 0" -t pytorch