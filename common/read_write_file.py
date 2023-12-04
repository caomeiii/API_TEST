# -*- coding: utf-8 -*-
"""
@Time:2023/9/1 13:48
@Auth:Dali
@QQ:1334029448
"""
from conf.config_path import get_path
class Read_Write_File():
    def __init__(self,*args):
        self.path=get_path(*args)
    def write_file(self,text):
        with open(self.path,'w',encoding='utf-8')as file_w:
            file_w.write(text)
    def read_file(self):
        with open(self.path,'r',encoding='utf-8')as file_r:
            return file_r.read()
if __name__ == '__main__':
    rwf=Read_Write_File('data','userid.txt')
    print(rwf.read_file())