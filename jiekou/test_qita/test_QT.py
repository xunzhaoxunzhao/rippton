import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json
class test_shegnhuo(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'
    def tearDown(self):
        pass

    def test_fabushenghuo(self):
        self.url = self.host+'/api/distributionother/v2/publish'
        self.shijan = xieru.xianzufangfaming(self)
        self.token = xieru.rwenjian(self)
        data = {
         'customerId':'975694035530285056',
            'content':self.shijan,
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result= self.r.json()
        self.assertEqual(self.result['code'],0)


    def test_shanchushegnhuo(self):
        '''删除发布的其他发布项, 仅限于其发布者可执行此操作'''
        self.url = self.host + '/api/distributionother/v2/deletion'
        self.shegnhuo = xieru.lianmysql_shegnhuoid(self)
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'otherItemId': self.shegnhuo,
            'token': self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

if __name__=='__main__':
    unittest.main()