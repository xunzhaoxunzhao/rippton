import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json

class testyonghu3(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'

    def tearDown(self):
        pass

    def test_chakanfenxiang(self):
        self.url=self.host+'/api/customer/v2/sharers'
        self.token=xieru.rwenjian(self)
        '''查看分享的鱼探'''
        data ={
            'customerId':'975694035530285056',
            'itemId':'983909208665620480',
            'token':self.token,
            'type':'2',
            'page':'1',
            'rows':'15',
        }
        self.r = requests.post(self.url,data=data)
        self.resul = self.r.json()
        self.assertEqual(self.resul['code'],0)
        '''查看分享的鱼获'''
        data2 = {
            'customerId': '975694035530285056',
            'itemId': '983909208665620480',
            'token': self.token,
            'type': '1',
            'page': '1',
            'rows': '15',
        }
        self.r2 = requests.post(self.url, data=data2)
        self.resul2 = self.r2.json()
        self.assertEqual(self.resul2['code'], 0)
        '''查看分享的经验'''
        data3 = {
            'customerId': '975694035530285056',
            'itemId': '983909208665620480',
            'token': self.token,
            'type': '3',
            'page': '1',
            'rows': '15',
        }
        self.r3 = requests.post(self.url, data=data3)
        self.resul3 = self.r3.json()
        self.assertEqual(self.resul3['code'], 0)
        '''查看分享的其他'''
        data4 = {
            'customerId': '975694035530285056',
            'itemId': '983909208665620480',
            'token': self.token,
            'type': '4',
            'page': '1',
            'rows': '15',
        }
        self.r4 = requests.post(self.url, data=data4)
        self.resul4 = self.r4.json()
        self.assertEqual(self.resul4['code'], 0)
        '''查看分享的活动'''
        data5 = {
            'customerId': '975694035530285056',
            'itemId': '983909208665620480',
            'token': self.token,
            'type': '5',
            'page': '1',
            'rows': '15',
        }
        self.r5 = requests.post(self.url, data=data5)
        self.resul5 = self.r5.json()
        self.assertEqual(self.resul5['code'], 0)

    @unittest.skip(u'暂时跳过')
    def test_tuichudengru(self):
        '''退出登入'''
        self.url=self.host+'/api/customer/v2/signout'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_jinrijifen(self):
        '''我的今日积分'''
        self.url = self.host+'/api/customer/v2/today/points'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_chaxundianzan(self):
        '''查询y鱼获点赞用户'''
        self.url =self.host+'/api/customer/v2/thumbnailers'
        self.token=xieru.rwenjian(self)
        data={
            'customerId':'975694035530285056',
            'itemId':'983952282406092800',
            'page':'1',
            'rows':'15',
            'type':'1',
            'token':self.token,
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
        '''查询鱼探点赞'''
        data2 = {
            'customerId': '975694035530285056',
            'itemId': '983952282406092800',
            'token': self.token,
            'type': '2',
            'page': '1',
            'rows': '15',
        }
        self.r2 = requests.post(self.url,data=data2)
        self.result2 = self.r2.json()
        self.assertEqual(self.result2['code'],0)
        '''查询经验点赞'''
        data3 = {
            'customerId': '975694035530285056',
            'itemId': '983952282406092800',
            'token': self.token,
            'type': '3',
            'page': '1',
            'rows': '15',
        }
        self.r3 = requests.post(self.url, data=data3)
        self.result3 = self.r3.json()
        self.assertEqual(self.result3['code'], 0)
        '''查询其他点赞'''
        data4 = {
            'customerId': '975694035530285056',
            'itemId': '983952282406092800',
            'token': self.token,
            'type': '4',
            'page': '1',
            'rows': '15',
        }
        self.r4 = requests.post(self.url, data=data4)
        self.result4= self.r4.json()
        self.assertEqual(self.result4['code'], 0)
        '''查询活动点赞'''
        data5 = {
            'customerId': '975694035530285056',
            'itemId': '983952282406092800',
            'token': self.token,
            'type': '5',
            'page': '1',
            'rows': '15',
        }
        self.r5 = requests.post(self.url, data=data5)
        self.result5= self.r5.json()
        self.assertEqual(self.result5['code'], 0)

if __name__=='__main__':
    unittest.main()