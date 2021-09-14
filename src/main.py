from . import argv
import os
import sys
import json
import csv
from . import dlprof_parser
from .show_gpu_info import show_gpu
from .profiling_command import *


def to_dict(result):
    tmp = dict()
    tmp["summary"] = list()
    for i in result:
        tmp["summary"].append(
            i.to_dict()
        )
    return tmp


def write2file(filename,fileformat,result):
    if(fileformat=="json"):
        result = to_dict(result)
        with open(filename+'.json', 'w+', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
    elif(fileformat=="csv"):
        with open(filename+'.csv', 'w+', encoding='UTF8') as f:
            writer = csv.writer(f)
            title = ["op type","gpu duration", "api call start", "kernel name"]
            writer.writerow(title)
            for i in result:
                writer.writerow(i.to_list())
    else:
        tmp = sys.stdout
        sys.stdout = open(filename, "w+")
        for i in result:
            i.printall()
        sys.stdout = tmp


def rm_log(verbose:bool):
    if(verbose):
        os.system("rm -rf log/")


def main():

    args = argv.argparsing()
    gpu = show_gpu(False)

    if(args.function=="gpuinfo"):
        for i in gpu:
            i.print_info()
    elif(args.function=="profile"):
    
        command = generate_command(args.model_type, args.gpu_idx,args.command)
        os.system(command)

        log_file_name = "log/dlprof_iteration.json"
        dlprof_result = dlprof_parser.parsing(log_file_name)
        write2file(args.output_filename, args.format, dlprof_result)

        rm_log(args.log)

if __name__ == "__main__":
    main()
