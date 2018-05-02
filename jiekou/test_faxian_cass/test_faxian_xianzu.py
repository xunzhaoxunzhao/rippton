import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json

class test_faxianxz(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'

    def tearDown(self):
        pass
    def test_genjuxianzufaxianyuershuju(self):
        '''根据线组查询鱼饵数据'''
        self.url = self.host+'/api/discovery/v2/related/rig/bait'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rigId':'2c928082615afb990161c6a300860049',
            'rows':'10',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_genjuxianzufaxianxianjie(self):
        '''根据线组查询鱼饵数据'''
        self.url = self.host+'/api/discovery/v2/related/rig/knot'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rigId':'2c928082615afb990161c6a300860049',
            'rows':'10',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_genjuxchazhaodiaofashuju(self):
        '''根据线组查询钓法数据'''
        self.url = self.host + '/api/discovery/v2/related/rig/method'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'page': '1',
            'rigId': '2c928082615afb990161c6a300860049',
            'rows': '10',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_diaodianguanlianyuer(self):
        '''钓点关联鱼饵'''
        self.url = self.host + '/api/discovery/v2/related/spot/bait'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'page': '1',
            'spotId':'956696529387651072',
            'rows': '10',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_diaodianguandiaofa(self):
        '''钓点关联钓法'''
        self.url = self.host + '/api/discovery/v2/related/spot/method'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'page': '1',
            'spotId': '956696529387651072',
            'rows': '10',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_diaodianguanxianzu(self):
        '''钓点关联线组'''
        self.url = self.host + '/api/discovery/v2/related/spot/rig'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'page': '1',
            'spotId': '956696529387651072',
            'rows': '10',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_xianzuliebiao(self):
        '''线组列表'''
        self.url = self.host + '/api/discovery/v2/rigs'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'page': '1',
            'rows': '10',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_diaoganliebiao(self):
        '''钓竿列表'''
        self.url = self.host + '/api/discovery/v2/rods'
        self.token = xieru.rwenjian(self)
        data = {
           'customerId':'975694035530285056',
           'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_sousuohuodong(self):
        '''搜索活动'''
        self.url = self.host +'/api/discovery/v2/search/activity'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'text':'A',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_sousuoyuer(self):
        '''搜索鱼饵'''

        self.url = self.host+'/api/discovery/v2/search/bait'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'text': 't',
            'token': self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_sousuochegnshi(self):
        '''搜索框搜索城市'''

        self.url = self.host+'/api/discovery/v2/search/city'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'text': 'a',
            'token': self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    #def test_sousuojingyan(self):
       # '''搜索框搜索海钓经验'''

      #  self.url = self.host+'/api/discovery/v2/search/city'
      #  self.token = xieru.rwenjian(self)
      #  data = {
        #    'customerId': '975694035530285056',
        #    'text': 'a',
        #    'token': self.token,
     #   }
        ## self.result = self.r.json()
     #   self.assertEqual(self.result['code'],0)

    def test_sousuoyulei(self):
        '''搜索框搜索鱼类'''

        self.url = self.host+'/api/discovery/v2/search/fish'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'text': 'a',
            'token': self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_sousuofangfa(self):
        '''搜索海钓方法'''

        self.url = self.host+'/api/discovery/v2/search/method'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'text': '5',
            'token': self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_sousuoxianzu(self):
        '''搜索线组'''

        self.url = self.host+'/api/discovery/v2/search/rig'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'text': 'r',
            'token': self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_yonghuzijibuhuodyuelei(self):
        '''用户捕获到的鱼类'''

        self.url = self.host+'/api/discovery/v2/self/capture/fish'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'token': self.token,
            'page':'1',
            'rows':'15',
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
if __name__=='__mian__':
    unittest.main()