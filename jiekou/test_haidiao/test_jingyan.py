import unittest
import requests
from jiekou.fengzhuang.fangfa import *
from jiekou.conf.env import *

class test_yh(unittest.TestCase):

    def setUp(self):
        self.host =Host

    def tearDown(self):
        pass


    def test_fabujingyan(self):
        '''发布海钓经验'''
        self.url = self.host +'/api/experience/v2/publish'
        self.token = xieru.rwenjian(self)
        self.tupian=xieru.zhuanmatupian(self)

        data = {
            'customerId':'975694035530285056',
            'title':'测试测试测试脚本测试',
            'token':self.token,
            'content':self.tupian,
            }
        self.r =requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_shanchujingyan(self):
        '''删除发布的海钓经验, 仅限于海钓经验的发布者可执行此操作'''
        self.url = self.host + '/api/experience/v2/deletion'
        self.token = xieru.rwenjian(self)
        self.jingyabn=xieru.lianmysql_jingyanid(self)
        data = {
            'customerId':'975694035530285056',
            'experienceId':self.jingyabn,
            'token':self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)
if __name__ == '__main__':
    unittest.main()