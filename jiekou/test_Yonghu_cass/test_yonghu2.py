import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json
class test_yonghu2(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'

    def tearDown(self):
        pass
    def test_fensi(self):
        '''粉丝'''
        self.url = self.host+'/api/customer/v2/follower/fans'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'20',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_dingwei(self):
        '''定位'''
        self.url=self.host+'/api/customer/v2/geo/position'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'latitude':'22',
            'longitude':'113',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_jingyanyujifenlishi(self):
        '''经验与积分历史记录'''
        self.url=self.host+'/api/customer/v2/history/points'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_xunzhang(self):
        '''勋章列表'''
        self.url=self.host+'/api/customer/v2/honor/medals'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_gerenxinxi(self):
        '''修改个人信息'''
        self.url=self.host+'/api/customer/v2/info/config'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_myfriend(self):
        '''c查询我的好友'''
        self.url=self.host+'/api/customer/v2/myfriends'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'page':'1',
            'rows':'15',
            'token': self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_leijidegnru(self):
        '''累计登入消息提示'''
        self.url=self.host+'/api/customer/v2/online/time'
        self.token=xieru.rwenjian(self)
        data = {
             'customerId': '975694035530285056',
            'token':self.token
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_dongjie(self):
        '''是否冻结'''
        self.url=self.host+'/api/customer/v2/query/frozen'
        self.token=xieru.rwenjian(self)

        data={
            'customerId': '975694035530285056',
            'token': self.token
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_tedingyonghu(self):
        '''特定id用户的用户详情, 避免与customerId冲突'''
        self.url=self.host+'/api/customer/v2/redundance'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'userId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
if __name__=='__main__':
    unittest.main()
