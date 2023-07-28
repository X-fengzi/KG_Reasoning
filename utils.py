import os
from easydict import EasyDict as edict
from collections import namedtuple
import argparse


def read_options():
    # 1. 定义命令行解析器对象
    parser = argparse.ArgumentParser(description='Demo of argparse')
    
    # 2. 添加命令行参数
    parser.add_argument('--epochs', type=int, default=30, help="max number of epochs")
    parser.add_argument('--batch', type=int, default=4, help="batch size")
    parser.add_argument('--steps', type=int, default=3, help="max steps of agent")

    return parser
 


def list_data_storage(data: list, file_path: str, file_name: str):

    # This function stores the secondary list data as a file, where each list is a row

    if not file_path.endswith('/'):
        file_path = file_path + '/'
    if os.path.exists(file_path):
        pass
    else:
        os.makedirs(file_path)
    file = file_path+file_name
    with open(file, 'a+') as f:
        for item in data:
            if isinstance(item,list):
                f.writelines(str.replace(str(item)[1:-1], ',', ' ')+'\n')
            else:
                f.writelines(str.replace(str(data)[1:-1], ',', ' ')+'\n')
                break
    f.close()

def Reward():
    pass


Transition = namedtuple(
    'Transition', ('state', 'action', 'next_state', 'reward'))

task = edict(mode=None,
             head=None,
             tail=None,
             query=None,
             cur_entity=None,
             transition=None,
             transitions=None)
