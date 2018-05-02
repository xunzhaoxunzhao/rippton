import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json

class test_faxianyulei(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'

    def tearDown(self):
        pass
    def test_yuleixiangqing(self):
        '''鱼类详情'''
        self.url = self.host+'/api/discovery/v2/fish/detail'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'fishId':'09230d16769f488196b96121ffbcf75e',
            'catchesId':'973769792177569792',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_haidiaojingyan(self):
        '''发现里海钓经验列表, 可按照发布用户id、线组id、鱼饵id和海钓方法id等条件过滤数据'''
        self.url = self.host+'/api/discovery/v2/fishingexperiences'
        self.token = xieru.rwenjian(self)
        data = {
            'page':'1',
            'rows':'15',
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_haidiaofangfa(self):
        '''海钓方法列表'''
        self.url = self.host+'/api/discovery/v2/fishingmethods'
        self.token = xieru.rwenjian(self)
        data = {
            'page':'1',
            'rows':'10',
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_haifuderen(self):
        '''获取用户附近的海钓爱好者，距离范围在1000公里以内'''
        self.url = self.host+'/api/discovery/v2/fishmen'
        self.token = xieru.rwenjian(self)
        data = {
            'page':'1',
            'rows':'20',
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_yuleileib(self):
        '''鱼类列表'''
        self.url = self.host+'/api/discovery/v2/fishspecies'
        self.token = xieru.rwenjian(self)
        data = {
            'isPublished':'0',
            'page':'1',
            'rows':'15',
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
        data2 = {
            'isPublished': '1',
            'page': '1',
            'rows': '15',
            'customerId': '975694035530285056',
            'token': self.token,
        }
        self.r2 = requests.post(self.url, data=data2)
        self.result2 = self.r2.json()
        self.assertEqual(self.result2['code'], 0)

    def test_youerliebiao(self):
        '''诱饵列表'''
        self.url = self.host+'/api/discovery/v2/lures'
        self.token = xieru.rwenjian(self)
        data = {
            'page':'1',
            'rows':'15',
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_jinfeiqu(self):
        '''查询禁飞区'''
        self.url = self.host+'/api/discovery/v2/noflyzone'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_genjuyuerchaxundiaofashuju(self):
        '''根据鱼饵查询钓法数据'''
        self.url = self.host+'/api/discovery/v2/related/bait/method'
        self.token = xieru.rwenjian(self)
        data = {
            'baitId':'2c92808261d5ef070161e0b537760066',
            'page':'1',
            'rows':'10',
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_genjuyuerchaxunxianzushuju(self):
        '''根据鱼饵查询线组数据'''
        self.url = self.host + '/api/discovery/v2/related/bait/rig'
        self.token = xieru.rwenjian(self)
        data = {
            'baitId': '2c92808261d5ef070161e0b537760066',
            'page': '1',
            'rows': '10',
            'customerId': '975694035530285056',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)
    def test_genjuchenshiguanlianyuer(self):
        '''根据城市查询关联鱼饵'''
        self.url = self.host + '/api/discovery/v2/related/city/bait'
        self.token = xieru.rwenjian(self)
        data = {
            'cityId':'dafb06ef4271425fb0550c41981d6125',
            'page': '1',
            'rows': '10',
            'customerId': '975694035530285056',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)
    def test_genjuchenshiguanliandiaofa(self):
        '''根据城市查询关联钓法'''
        self.url = self.host + '/api/discovery/v2/related/city/method'
        self.token = xieru.rwenjian(self)
        data = {
            'cityId':'dafb06ef4271425fb0550c41981d6125',
            'page': '1',
            'rows': '10',
            'customerId': '975694035530285056',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_genjuchenshiguanlianxianzhu(self):
        '''根据城市查询关联线组'''
        self.url = self.host + '/api/discovery/v2/related/city/rig'
        self.token = xieru.rwenjian(self)
        data = {
            'baitId':'2c92808261d5ef070161e0b537760066',
            'page': '1',
            'rows': '10',
            'customerId': '975694035530285056',
            'token': self.token,
            'cityId':'dafb06ef4271425fb0550c41981d6125',
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_genjudiaofachaxunyuershuju(self):
        '''根据钓法查询鱼饵数据'''
        self.url = self.host + '/api/discovery/v2/related/method/bait'
        self.token = xieru.rwenjian(self)
        data = {
            'methodId': '2c92808260ed97530160f8883511007b',
            'page': '1',
            'rows': '10',
            'customerId': '975694035530285056',
            'token': self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_genjudiaofachaxunxianzushuju(self):
        '''根据钓法查询线组数据'''
        self.url = self.host + '/api/discovery/v2/related/method/rig'
        self.token = xieru.rwenjian(self)
        data = {
            'methodId': '2c92808261d5ef070161e0ace9670061',
            'page': '1',
            'rows': '10',
            'customerId': '975694035530285056',
            'token': self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)




if __name__=='__main__':
    unittest.main()