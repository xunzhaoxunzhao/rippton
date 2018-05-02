import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json
from jiekou.conf.env import *

class test_GZ(unittest.TestCase):
    def setUp(self):
        self.host=Host
    def tearDown(self):
        pass
    def test_guanzhuhuodong(self):
        '''关注的活动数据'''

        self.url = self.host+'/api/focusitem/v2/following/activities'
        self.token= xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_guanzhuyuershuju(self):
        '''关注的鱼饵数据'''

        self.url = self.host+'/api/focusitem/v2/following/bait'
        self.token= xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'10',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_guanzhuyongshu(self):
        '''统计用户关注项的关注数量'''

        self.url = self.host+'/api/focusitem/v2/following/counter'
        self.token= xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
           # 'page':'1',
          #  'rows':'10',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_guanzhuyuleishuju(self):
        '''关注的鱼类数据'''

        self.url = self.host+'/api/focusitem/v2/following/fish'
        self.token= xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_guanzhudiaofa(self):
        '''关注的钓法数据'''

        self.url = self.host+'/api/focusitem/v2/following/method'
        self.token= xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'10',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_guanzhuxianzu(self):
        '''关注的线组数据'''

        self.url = self.host+'/api/focusitem/v2/following/rig'
        self.token= xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'10',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_guanzhuxyonghu(self):
        '''关注的用户数据'''

        self.url = self.host+'/api/focusitem/v2/following/user'
        self.token= xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'20',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_shifangchangdu(self):
        '''根据鱼类id和地区id，查询鱼类释放的最小长度'''
        self.url=self.host+'/api/lengthrule/v2/query/rule'
        self.token=xieru.rwenjian(self)
        data = {
            'regionId':'cecc61c2421047ec8daf494408c0c768',
            'fishId':'09230d16769f488196b96121ffbcf75e',
            'customerId': '975694035530285056',
            'token': self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

if __name__=='__main__':
    unittest.main()