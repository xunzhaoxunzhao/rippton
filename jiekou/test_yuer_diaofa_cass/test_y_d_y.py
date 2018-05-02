import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json
class test_yu_diaofa_yushe(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'
    def tearDown(self):
        pass

    def test_yuzhizhuhe(self):
        '''预设置组合列表'''
        self.url= self.host+'/api/combination/v2/combinations'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'token':self.token,
            'page':'1',
            'rows':'15'
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_chaungjianzhuhe(self):
        '''创建线组、海钓方法、鱼饵、钓杆、诱饵、无人机等预设置组合'''
        self.url=self.host+'/api/combination/v2/creation'
        self.token = xieru.rwenjian(self)
        self.mingzi=xieru.xianzufangfaming(self)
        data={
            'customerId':'975694035530285056',
            'name':self.mingzi,
            'token':self.token,
            'methodId':'297ecff962088a6c0162088c7cc60002',
        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
        #return self.mingzi
    def test_shanchuzuhe(self):
        '''删除预设置组合'''
        self.url = self.host+'/api/combination/v2/deletion'
        self.token=xieru.rwenjian(self)
        data = {
            'combinationId':'984019753334996992',
            'customerId':'975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_xiugai(self):
        '''修改线组、海钓方法、鱼饵、钓杆、诱饵、无人机等预设置组合'''
        self.url = self.host+'/api/combination/v2/modification'
        self.token = xieru.rwenjian(self)
        self.neme=xieru.xianzufangfaming(self)
        self.name=str(self.neme)+'a'
        data = {
            'combinationId':'984020850581700608',
            'customerId':'975694035530285056',
            'methodId':'297ecff962088a6c0162088c7cc60002',
            'name':self.name,
            'rigId':'2c92808260ed97530160f8889c4c007d',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)

if __name__=='__main__':
    unittest.main()