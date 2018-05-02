import unittest
import requests
import hashlib
from jiekou.fengzhuang.fangfa import *
from jiekou.conf.env import *
class test_yonghu(unittest.TestCase):
    def setUp(self):
        '''密码加密'''
        self.host = 'http://10.156.0.100:8080/rippton2nd'


    def tearDown(self):
        pass

    #@unittest.skip(u'强制跳过')
    def test_dengru(self):
        '''用户登入'''
        self.url = self.host+'/api/customer/v2/signin'
        #session1 = requests.Session()
        #session1.post(self.url)
        self.password = xieru.mima(self)
        data = {
            'deviceToken':'asdfghjkl',
            'deviceType':'iphone',
            'email':'970404223@qq.com',
            'passwd':self.password
        }
        #self.r = session1.post(self.url,data=data)
        self.r = requests.post(self.url,data=data)
        #print(self.r.text)
        self.result=self.r.json()
        self.token = self.result['data']['token']
        self.wenjian=open('C:/token/token.txt','w+')
        self.wenjian.write(self.token)
        self.wenjian.close()
        self.assertEqual(self.result['code'],0,msg='正确')

    #@unittest.skip(u'强制跳过')
    def test_wurenji(self):
        '''无人机'''
        self.url=self.host+'/api/customer/v2/connected/drones'
        self.token =xieru().rwenjian()
        print(self.token)
        data = {
            'customerId':'975694035530285056',
           # 'page':'0',
            #'rows':'15',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0,msg='duos')
        self.assertEqual(self.result['msg'],'success',msg='success')

    #@unittest.skip(u'强制跳过')
    def test_shuruyanzm(self):
        self.url=self.host + '/api/customer/v2/code'
       # self.token=xieru.rwenjian(self)
       # print(self.token)
        '''注册时的验证码'''
        data1 = {
            'email':'970404223@qq.com',
            'operation':'signup'
        }
        self.r=requests.post(self.url,data=data1)

        self.result=self.r.json()
        print(self.result)
        self.assertEqual(self.result['code'],0)
        '''更改密码'''
        data2={
            'email':'970404223@qq.com',
            'operation':'updatepwd'
        }
        self.r2=requests.post(self.url,data=data2)
        self.result2=self.r.json()
        self.assertEqual(self.result2['code'],0)
        '''忘记密码'''
        data3 = {
            'email': '970404223@qq.com',
            'operation': 'forgetpwd'
        }
        self.r3 = requests.post(self.url, data=data3)
        self.result3 = self.r.json()
        self.assertEqual(self.result3['code'], 0)
        '''更改邮箱'''
        data4 = {
            'email': '970404223@qq.com',
            'operation': 'updateemail'
        }
        self.r4 = requests.post(self.url, data=data4)
        self.result4 = self.r.json()
        self.assertEqual(self.result4['code'], 0)

    #@unittest.skip(u'强制跳过')
    def test_shouchang(self):
        '''所有收藏'''
        self.url=self.host+'/api/customer/v2/favorite/items'
        self.token=xieru.rwenjian(self)
        data ={
            'customerId':'975694035530285056',
            'type':'0',
            'page':'1',
            'rows':'15',
            'token':self.token
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
        '''鱼获收藏'''
        data2 = {
            'customerId': '975694035530285056',
            'type': '1',
            'page': '1',
            'rows': '15',
            'token': self.token
        }
        self.r2 = requests.post(self.url, data=data2)
        self.result2 = self.r2.json()
        self.assertEqual(self.result2['code'], 0)
        '''鱼探收藏'''
        data3= {
            'customerId': '975694035530285056',
            'type': '2',
            'page': '1',
            'rows': '15',
            'token': self.token
        }
        self.r3 = requests.post(self.url, data=data3)
        self.result3 = self.r3.json()
        self.assertEqual(self.result3['code'], 0)
        '''海钓经验'''
        data4 = {
            'customerId': '975694035530285056',
            'type': '3',
            'page': '1',
            'rows': '15',
            'token': self.token
        }
        self.r4 = requests.post(self.url, data=data4)
        self.result4 = self.r4.json()
        self.assertEqual(self.result4['code'], 0)
        '''其他'''
        data5 = {
            'customerId': '975694035530285056',
            'type': '4',
            'page': '1',
            'rows': '15',
            'token': self.token
        }
        self.r5 = requests.post(self.url, data=data5)
        self.result5 = self.r5.json()
        self.assertEqual(self.result5['code'], 0)


if __name__=='__mian__':
    unittest.main()
