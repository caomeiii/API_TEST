# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 16:47
@Auth:Dali
@QQ:1334029448
"""
import os

base_path=os.path.dirname(os.path.dirname(__file__))

def get_path(*args):#获取文件路径
    return os.path.join(base_path,*args)
if __name__ == '__main__':
    print(get_path('data','header.yaml'))