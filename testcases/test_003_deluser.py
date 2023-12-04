# -*- coding: utf-8 -*-
"""
@Time:2023/9/1 11:30
@Auth:Dali
@QQ:1334029448
"""
from common.request_api import Api as api
from utils.read_excel import Read_Excel
from common.read_write_file import Read_Write_File
from db.read_sql_data import Test_Sql
rwf=Read_Write_File('data','userid.txt')
import pytest
read_e=Read_Excel()
class Test_Deluser():
    @pytest.mark.parametrize('body',read_e.get_body(4))
    def test_deluser(self,body):
        # print(body[0])
        if body[0]['ids']=='10086':
            # body[0]['ids']=rwf.read_file()
            body[0]['ids'] = Test_Sql().select_userid()
        resp=api.post(url=read_e.get_url(4),data=body[0])
        print(resp.json())

if __name__ == '__main__':
    pytest.main(['-vs',r'D:\class_project\class_70\class_70_api_frame\testcases'])