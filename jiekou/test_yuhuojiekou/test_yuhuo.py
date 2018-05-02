import unittest
import requests
from jiekou.fengzhuang.fangfa import *

class test_yh(unittest.TestCase):

    def setUp(self):
        self.host ='http://10.156.0.100:8080/rippton2nd'

    def tearDown(self):
        pass

    def test_guolvyuhuo(self):
        '''按鱼获长度倒序排序鱼获, 同时还可根据发布人、鱼类、城市、和活动条件过滤数据'''

        self.url = self.host+'/api/fishcatches/v2/capture/all/rank'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'fishId':'93dcff39fb5d4396ac3ac20784264fbf',
            'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)


    def test_yuhuoshijian(self):
        '''按时间倒序鱼获, 同时还可根据发布人、鱼类、城市、和活动条件过滤数据'''

        self.url = self.host+'/api/fishcatches/v2/capture/all/time/rank'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'fishId':'93dcff39fb5d4396ac3ac20784264fbf',
            'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_fabuyuhuo(self):
        '''发布鱼获'''

        self.url = self.host+'/api/fishcatches/v2/publish'
        self.token=xieru.rwenjian(self)
        self.tupian = xieru.zhuanmatupian(self)
        data = {
            'customerId':'975694035530285056',
            'isLeaderboard':'1',
            'fishId':'93dcff39fb5d4396ac3ac20784264fbf',
            'fishName':'Amberjack',
            'groupPhotos':self.tupian,
            'lenPic':self.tupian,
            'fishLength':'234',
            'catchTimeNum':'1524131400',
            'cityId':'1c03a3b51c0c414aa1fd77a0a9466508',
            'isRelease':'1',
            'token':self.token,
            'baitId':'2c92808261d5ef070161e0b619030068',
            'baitName':'小泥鳅',
            'methodId':'297ecff962088a6c0162088c7cc60002',
            'methodName':'566',
            'rigId':'2c928082615afb990161c6a300860049',
            'rigName':'rig123456790+1234567890+123456',
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)


    def test_chaxunyuer(self):
        '''根据鱼类查询鱼饵'''
        self.url=self.host+'/api/fishcatches/v2/related/fish/bait'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'fishId':'93dcff39fb5d4396ac3ac20784264fbf',
            'page':'1',
            'rows':'10',
            'token':self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_chaxundiaofa(self):
        '''根据鱼类查询钓法'''
        self.url = self.host + '/api/fishcatches/v2/related/fish/method'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'fishId': '93dcff39fb5d4396ac3ac20784264fbf',
            'page': '1',
            'rows': '10',
            'token': self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_chaxunxianzhu(self):
        '''根据鱼类查询线组'''
        self.url = self.host + '/api/fishcatches/v2/related/fish/rig'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId': '975694035530285056',
            'fishId': '93dcff39fb5d4396ac3ac20784264fbf',
            'page': '1',
            'rows': '10',
            'token': self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_shanchuyuhuo(self):
        '''删除发布的鱼获, 仅限于鱼获的发布者可执行此操作'''
        self.url =self.host+'/api/fishcatches/v2/deletion'
        self.token=xieru.rwenjian(self)
        self.yuhuoid=xieru.lianmysql_yuhuoid(self)
        data = {
            'catchesId':self.yuhuoid,
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)

    def test_paihangbang(self):
        '''排行榜鱼获世界第一的鱼获列表'''
        self.url = self.host+'/api/fishcatches/v2/leaderboard/cover/catches'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_yonghupaimingkaoqiandeyuhuo(self):
        '''用户排名最靠前的鱼获'''
        self.url = self.host+'/api/fishcatches/v2/self/bestcatches'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token,
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_wodeyuhuopaimingpegnyouquan(self):
        '''我的鱼获排名朋友圈'''
        self.url = self.host+'/api/fishcatches/v2/self/catches/rank'
        self.token=xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token,
            'fishId':'all',
            'isFriendRank':'1',
            'page':'1',
            'rows':'15',
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_wodeyuhuopaimingbushipengyouquan(self):
        '''我的鱼获排名不是朋友圈'''
        self.url = self.host + '/api/fishcatches/v2/self/catches/rank'
        self.token = xieru.rwenjian(self)
        data = {
                'customerId': '975694035530285056',
                'token': self.token,
                'fishId': 'all',
                'isFriendRank': '0',
                'page': '1',
                'rows': '15',
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)
    def test_diaodianxiangguanyuhuo(self):
        '''钓点相关的鱼获'''
        self.url = self.host + '/api/fishcatches/v2/spot/catches'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'page':'1',
            'rows':'15',
            'spotId':'984696828328935424',
            'token':self.token
        }
        self.r = requests.post(self.url, data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'], 0)
if __name__=='__main__':
    unittest.main()