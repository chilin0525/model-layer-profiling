import argv
import os
import dlprof_parser
from show_gpu_info import show_gpu
from profiling_command import *

def main():

    # args = argv.argparsing()
    # gpu = show_gpu(args.gpuinfo)

    # command = generate_command(args.model_type, args.path, args.gpu_idx)
    # os.system(command)

    log_file_name = "log/dlprof_iteration.json"
    result = dlprof_parser.parsing(log_file_name)
    for i in result:
        i.printall()

if __name__ == "__main__":
    main()
