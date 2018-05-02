import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json

class test_FX(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'

    def tearDown(self):
        pass

    def test_huodonglieb(self):
        '''所有活动列表'''
        self.url = self.host+'/api/discovery/v2/activities'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'15',
            'state':'1',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
        '''比赛活动未开始'''
        data2 = {
            'customerId': '975694035530285056',
            'page': '1',
            'rows': '15',
            'state': '2',
            'token': self.token,
        }
        self.r2 = requests.post(self.url, data=data2)
        self.result2 = self.r2.json()
        self.assertEqual(self.result2['code'], 0)
        '''比赛活动正在进行中'''
        data3 = {
            'customerId': '975694035530285056',
            'page': '1',
            'rows': '15',
            'state': '3',
            'token': self.token,
        }
        self.r3 = requests.post(self.url, data=data3)
        self.result3 = self.r3.json()
        self.assertEqual(self.result3['code'], 0)
        '''比赛活动已经结束'''
        data4 = {
            'customerId': '975694035530285056',
            'page': '1',
            'rows': '15',
            'state': '4',
            'token': self.token,
        }
        self.r4 = requests.post(self.url, data=data4)
        self.result4 = self.r4.json()
        self.assertEqual(self.result4['code'], 0)

    def test_huodongxiangqing(self):
        '''活用详情'''
        self.url = self.host+'/api/discovery/v2/activity/detail'
        self.token=xieru.rwenjian(self)
        data = {
            'activityId':'2c9280826101f31f0161024007f7001a',
            'customerId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)


    def test_buhuoyulei(self):
        '''捕获鱼类'''
        self.url = self.host+'/api/discovery/v2/all/capture/fish'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_fishidchegnshi(self):
        '''根据鱼类查询鱼获的城市列表'''
        self.url = self.host+'/api/discovery/v2/all/fishcatch/cities'
        self.token = xieru.rwenjian(self)
        data = {
            'fishId':'c1a67f1661d04927b42b02555bedcb3e',
            'token':self.token,
            'customerId':'975694035530285056',
        }
        self.r = requests.post(self.url,data=data)
        print(self.r.text)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_yuer(self):
        '''鱼饵详情'''
        self.url = self.host+'/api/discovery/v2/bait/detail'
        self.token = xieru.rwenjian(self)
        data = {
            'baitId':'2c92808261d5ef070161e0b619030068',
            'token':self.token,
            'customerId':'975694035530285056',
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_yuerliebiao(self):
        '''鱼饵列表'''
        self.url = self.host+'/api/discovery/v2/baits'
        self.token = xieru.rwenjian(self)
        data = {
          'customerId':'975694035530285056',
            'page':'1',
            'rows':'10',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_lubo(self):
        '''Banner广告详情'''
        self.url = self.host+'/api/discovery/v2/banner/detail'
        self.token = xieru.rwenjian(self)
        data = {
            'bannerId':'2c9280826242550b01624791620a002d',
             'customerId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_luboguangkaoshuju(self):
        '''Banner广告数据'''
        self.url = self.host+'/api/discovery/v2/banners'
        self.token = xieru.rwenjian(self)
        data = {
            'rows':'5',
             'customerId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_suozaichegnshi(self):
        '''所有城市的列表'''
        self.url = self.host+'/api/discovery/v2/cities'
        self.token = xieru.rwenjian(self)
        data = {

             'customerId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        #print(self.r.text)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_guojiachegnshi(self):
        '''国家或城市详情'''
        self.url = self.host+'/api/discovery/v2/city/detail'
        self.token = xieru.rwenjian(self)
        data = {
                'cityId':'1c03a3b51c0c414aa1fd77a0a9466508',
             'customerId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
       # print(self.r.text)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_guojiashujubanben(self):
        '''国家城市的数据版本'''
        self.url = self.host + '/api/discovery/v2/cityData/version'
        self.token = xieru.rwenjian(self)
        data = {

            'customerId': '975694035530285056',
            'token': self.token
        }
        self.r = requests.post(self.url, data=data)
       # print(self.r.text)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)
#    def test_wurenjixinghao(self):
 #       '''无人机型号详情'''
      #  self.url = self.host + ' /api/discovery/v2/drone/detail '
       # self.token = xieru.rwenjian(self)
        #data = {
         #   'droneId':'2c9280826242550b0162475cd204002b',
          #  'customerId': '975694035530285056',
         #   'token': self.token
        #}
        #self.r = requests.post(self.url, data=data)
        #print(self.r.text)
        #self.result = self.r.json()
        #self.assertEqual(self.result['code'], 0)
    def test_wurenjixinghaoliebiao(self):
        '''无人机型号列表'''
        self.url = self.host + '/api/discovery/v2/drones'
        self.token = xieru.rwenjian(self)
        data = {

            'customerId': '975694035530285056',
            'token': self.token,
            'page':'0',
            'rows':'15'
        }
        self.r = requests.post(self.url, data=data)
        # print(self.r.text)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_faxianrukou(self):
        '''发现模块入口列表'''
        self.url = self.host + '/api/discovery/v2/entry/index'
        self.token = xieru.rwenjian(self)
        data = {

            'customerId': '975694035530285056',
            'token': self.token,
            #'page':'0',
          #  'rows':'15'
        }
        self.r = requests.post(self.url, data=data)
        # print(self.r.text)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

if __name__=='__main__':
    unittest.main()