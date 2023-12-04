# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 17:53
@Auth:Dali
@QQ:1334029448
"""
import requests
class Api():
    session=requests.Session()

    @classmethod
    def post(cls,url,**kwargs):
        return cls.session.post(url,**kwargs)

    @classmethod
    def get(cls,url,**kwargs):
        return cls.session.get(url,**kwargs)