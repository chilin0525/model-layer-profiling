import argparse

def argparsing():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--command", dest="command", 
        help="whole inference script")
    parser.add_argument(
        "-t", "--model_type", choices=["pytorch", "onnx", "tensorrt"], dest="model_type",
        help="specify pretrained model type")
    parser.add_argument(
        "-o", "--output", default="layer_inference_result", dest="output_filename", type=str,
        help="specify output file name, default is \"layer_inference_result\"")
    parser.add_argument(
        "-f", "--format", choices=["json", "csv", "stdout"], dest="format", required=False,
        help="specify output file format, default is stdout", default="stdout")
    parser.add_argument("-g", "--gpu", dest="gpu_idx", default="0", type=str,
        help="set up gpu index to do inference, show gpu info by using: --gpuinfo")
    parser.add_argument("--gpuinfo", action="store_true", default=False, help="show gpu infomation")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    argparsing()
  
