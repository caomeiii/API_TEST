# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 16:24
@Auth:Dali
@QQ:1334029448
"""
import pytest,time,os
from conf.config_path import get_path
from utils.email_new import Test_Email
def runner():
    report_path=get_path("report",f"cases_{time.strftime('%Y%m%d%H%M%S')}report.html")
    pytest.main(['-vs',get_path('testcases'),f'--html={report_path}','--self-contained-html'])
    Test_Email(report_path).send_email()

    # pytest.main(['-vs', '--alluredir', './report/result'])
    # os.system('allure serve ./report/result')

if __name__ == '__main__':
    runner()