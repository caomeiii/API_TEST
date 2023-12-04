# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 16:54
@Auth:Dali
@QQ:1334029448
"""
import xlrd
from conf.config_path import get_path
from utils.read_yaml import Read_Yaml
'''读取excel表格'''

class Read_Excel():
    def __init__(self):
        self.read_y=Read_Yaml('data','data_new.yaml')
        book=xlrd.open_workbook(get_path('data','Data.xlsx'))
        self.sheet=book.sheet_by_index(0)
        self.case_id=0
        self.url=2
        self.params=4
    def get_value(self,row,col):
        return self.sheet.cell_value(row,col)
    def get_url(self,row):#获取url
        return self.get_value(row,self.url)
    def get_params(self,row):#获取params
        return self.get_value(row,self.params)

    def get_body(self,row):#通过get_params映射的方式取到值
        return self.read_y.read_dict()[self.get_params(row)]

if __name__ == '__main__':
    read_e=Read_Excel()
    print(read_e.get_params(2))
    print(read_e.get_body(1))