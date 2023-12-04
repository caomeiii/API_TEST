# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 18:00
@Auth:Dali
@QQ:1334029448
"""
from common.request_api import Api as api
from utils.read_excel import Read_Excel
from common.update_ini import set_ini
import pytest,logging
read_e=Read_Excel()
set_ini()
class Test_login():
    @pytest.mark.parametrize('body',read_e.get_body(1))
    def test_login(self,body):
        # print(body[0])
        resp=api.post(url=read_e.get_url(1),data=body[0])
        logging.info(resp.json())
        assert body[1]['code']==resp.json()['code']

if __name__ == '__main__':
    pytest.main(['-vs',r'D:\class_project\class_70\class_70_api_frame\testcases\test_001_login.py'])