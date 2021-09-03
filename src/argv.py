import argparse

def argparsing():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--path", dest="path", required=True, 
        help="specify your pretrained model path", )
    parser.add_argument(
        "-t", "--model_type", choices=["pytorch", "onnx", "tensorrt"], dest="model_type", required=True,
        help="specify pretrained model type")
    # parser.add_argument(
    #     "-r", "--runtime", choices=["pytorch", "onnxruntime", "tensorrt"], dest="runtime", required=False, 
    #     help="specify runntime platform")
    parser.add_argument(
        "-o", "--output", choices=["json", "csv", "stdout"], dest="output", required=False,
        default="stdout", help="specify output file format")
    parser.add_argument("-g", "--gpu", dest="gpu_idx", default="0", type=str,
        help="set gpu index to do inference, show gpu info by using: --gpuinfo")
    parser.add_argument("--gpuinfo", action="store_true", default=False, help="show gpu infomation")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    argparsing()
  
