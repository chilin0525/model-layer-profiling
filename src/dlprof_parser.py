import json
import sys


class node:
    def __init__(self, api_call_start, op_type, gpu_duration, kenrel_name):
        self.api_call_start = api_call_start
        self.op_type = op_type
        self.gpu_duration = gpu_duration
        self.kenrel_name = kenrel_name

    def __lt__(self, other):
        return self.api_call_start < other.api_call_start

    def printall(self):
        print("%-60s %-15d %-10d %s" %
            (self.op_type, self.api_call_start,self.gpu_duration, self.kenrel_name))

    def to_dict(self):
        tmp = {"Op Type": self.op_type.replace('"',""),
               "GPU Duration(ns):": self.gpu_duration,
               "API Call Start (ns)": self.api_call_start,
               "Long Kernel Name": self.kenrel_name.replace('"', "")}
        return tmp
    def to_list(self):
        return [self.op_type.replace('"', ""), self.gpu_duration,
                self.api_call_start, self.kenrel_name.replace('"', "")]

def parsing(file_path):

    with open(file_path, newline='') as jsonfile:
        data = json.load(jsonfile)

    nodes = list()
    data = data["Iteration Report"]
    for i in data:
        nodes.append(node(i["API Call Start (ns)"], i["Op Type"],
                        i["GPU Duration (ns)"], i["Long Kernel Name"]))

    nodes.sort()
    return nodes
