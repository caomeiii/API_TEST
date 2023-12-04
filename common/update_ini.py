# -*- coding: utf-8 -*-
"""
@Time:2022/2/22 10:56
@Auth:Dali
@QQ:1334029448
"""
from time import strftime
import configparser
from conf.config_path import get_path

conf=configparser.ConfigParser()#实例化配置文件的类

ini_path=get_path('pytest.ini')#获取ini文件据对路径
# print(ini_path)
def read_ini():
    conf.read(ini_path,encoding='utf-8')#打开文件
    #获取文件里面节点对应的项的值
    return (conf.get('pytest','log_file'))

def set_ini():
    conf.read(get_path('pytest.ini'),encoding='utf-8')
    now_time=strftime('%Y_%m_%d_%H_%M_%S')
    conf.set('pytest','log_file',rf'{get_path("log")}\{now_time}_test.log')
    conf.write(open(get_path('pytest.ini'),'r+',encoding='utf-8'))

if __name__ == '__main__':
    set_ini()
    print(read_ini())