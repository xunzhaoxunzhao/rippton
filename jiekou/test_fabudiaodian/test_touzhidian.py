import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json
from jiekou.conf.env import *
class test_shegnhuo(unittest.TestCase):
    def setUp(self):
        self.host = Host
    def tearDown(self):
        pass

    def test_fabutzd(self):
        '''发布探点'''
        self.url = self.host + '/api/fishingspot/v2/publish'
        self.token = xieru.rwenjian(self)
        self.tupian = xieru.zhuanmatupian(self)
        data = {
         'cityId':'7e0f74d8b82643aca60122d0b9feabd2',
            'content':'测试测试脚本测试',
            'crossSectionPic':self.tupian,
            'customerId':'975694035530285056',
            'discoveryTimeNum':'1524459456',
            'isFishingPoint':'0',
            'visibility':'1',
            'latitude':'22.587291',
            'longitude':'114.280774',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_shanchudiaodian(self):
        '''删除探点'''
        self.url=self.host+'/api/fishingspot/v2/deletion'
        self.token=xieru.rwenjian(self)
        self.spot = xieru.lianmysql_tandian(self)
        data = {
            'token':self.token,
            'customerId':'975694035530285056',
            'fishingSpotId':self.spot
        }
        self.r =requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_zhidingyuhuodiaodian(self):
        '''捕获到指定鱼类的钓点分布图'''
        self.url=self.host+'/api/fishingspot/v2/fish/distribution'
        self.token=xieru.rwenjian(self)
        data = {
            'bottomLatitue':'20.04435662298022',
            'customerId':'975694035530285056',
            'fishId':'93dcff39fb5d4396ac3ac20784264fbf',
            'zoom':'7',
            'topLongitue':'116.0730899793482',
            'topLatitue':'24.91512053724517',
            'bottomLongitue':'111.8543400206179',
            'token':self.token

        }
        self.r = requests.post(self.url,data=data)
        self.result =self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_paihangbangyutan(self):
        '''排行榜鱼探最近发布的鱼探列表'''
        self.url=self.host+'/api/fishingspot/v2/leaderboard/cover/spot'
        self.token=xieru.rwenjian(self)
        data = {
            'token':self.token,
            'customerId':'975694035530285056',

        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_guojiayutanpaihang(self):
        '''在所选国家或城市范围内钓点排名列表'''
        self.url = self.host+'/api/fishingspot/v2/leaderboard/scope/spots'
        self.token = xieru.rwenjian(self)
        data = {
            'token': self.token,
            'customerId': '975694035530285056',
            'page':'1',
            'rows':'15',

        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_ditushangdediaodian(self):
        '''海钓地图所有钓点, 包括我的钓点、我保存的钓点和其他钓点, 可根据特定城市过滤钓点'''

        self.url = self.host+'/api/fishingspot/v2/mapspot/all'
        self.token = xieru.rwenjian(self)
        data = {
            'token': self.token,
            'customerId': '975694035530285056',
            'bottomLatitue':'21.26565658288574',
            'bottomLongitue':'111.6552599322247',
            'topLongitue':'115.8740098909507',
            'topLatitue':'26.30999300226568',
            'zoom':'7',

        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_sousuotandian(self):
        '''搜索海钓地图的钓点'''
        self.url = self.host+'/api/fishingspot/v2/search/spot'
        self.token=xieru.rwenjian(self)
        data = {
            'token': self.token,
            'customerId': '975694035530285056',
            'text':'fir last',
            'zoom':'0'
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)


    def test_sousuoyonghu(self):
        '''搜索钓点用户'''
        self.url = self.host+'/api/fishingspot/v2/search/spot/user'
        self.token=xieru.rwenjian(self)
        data = {
            'token': self.token,
            'customerId': '975694035530285056',
            'text':'fir last',

        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_yonghukaoqiandetandian(self):
        '''用户排名最靠前的钓点'''
        self.url = self.host+'/api/fishingspot/v2/self/bestspot'
        self.token=xieru.rwenjian(self)
        data = {
            'token': self.token,
            'customerId': '975694035530285056',

        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_fabuyuhuoshidiandiao(self):
        '''发布鱼获时选钓点, 根据地图放大等级，取鱼探经纬度信息供在地图上定位鱼探点'''
        self.url = self.host+'/api/fishingspot/v2/spotMap'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'zoom':'7',
            'topLongitue':'116.0523749793238',
            'topLatitue':'24.75012143448399',
            'bottomLongitue':'111.8336250205846',
            'bottomLatitue':'20.28620693654294',
            'token':self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)
if __name__=='__main__':
    unittest.main()