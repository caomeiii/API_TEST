# -*- coding: utf-8 -*-
"""
@Time:2023/9/1 10:08
@Auth:Dali
@QQ:1334029448
"""
from common.request_api import Api as api
from utils.read_excel import Read_Excel
import pytest,faker,pprint,logging
from common.read_write_file import Read_Write_File
name=faker.Faker().name()
read_e=Read_Excel()
rwf=Read_Write_File('data','userid.txt')
class Test_Add_Query():
    @pytest.mark.parametrize('body',read_e.get_body(2))
    def test_adduer(self,body):
        if body[0]['userAccount']=='None':
            body[0]['userAccount']=name
            body[0]['userName']=name
        resp=api.post(url=read_e.get_url(2),data=body[0])
        logging.info(resp.json())
        assert body[1]['code'] == resp.json()['code']
    # @pytest.mark.skip()
    @pytest.mark.parametrize('body',read_e.get_body(3))
    def test_query(self,body):
        resp=api.post(url=read_e.get_url(3),data=body[0])
        # if resp.json()['model']['userList']:
            # rwf.write_file(str(resp.json()['model']['userList'][0]['id']))
if __name__ == '__main__':
    pytest.main(['-vs',r'D:\class_project\class_70\class_70_api_frame\testcases'])