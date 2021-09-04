import argv
import os
import sys
import dlprof_parser
from show_gpu_info import show_gpu
from profiling_command import *

def write2file(filename,result):
    tmp = sys.stdout
    sys.stdout = open(filename, "w+")
    for i in result:
        i.printall()
    sys.stdout = tmp

def main():

    args = argv.argparsing()
    gpu = show_gpu(args.gpuinfo)

    command = generate_command(args.model_type, args.gpu_idx,args.command)
    os.system(command)

    log_file_name = "log/dlprof_iteration.json"
    dlprof_result = dlprof_parser.parsing(log_file_name)
    write2file(args.output_filename, dlprof_result)

if __name__ == "__main__":
    main()
