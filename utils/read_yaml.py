# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 17:25
@Auth:Dali
@QQ:1334029448
"""
import yaml
from conf.config_path import get_path
class Read_Yaml():
    def __init__(self,*args):
        self.path=get_path(*args)
    def read_dict(self):#读取yaml文件为字典格式
        with open(self.path, 'r', encoding='utf-8') as file_r:
            return yaml.safe_load(file_r)
    def read_list(self):#读取yaml为列表格式
        with open(self.path, 'r', encoding='utf-8') as file_r:
            return list(yaml.full_load_all(file_r))
if __name__ == '__main__':
    read_y=Read_Yaml('data','data_new.yaml')
    print(type(read_y.read_dict()['case_001_login']),read_y.read_dict()['case_001_login'])

