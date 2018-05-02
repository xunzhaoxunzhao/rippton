import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json
import re

class test_H(unittest.TestCase):
    def setUp(self):
        self.host= 'http://10.156.0.100:8080/rippton2nd'

    def tearDown(self):
        pass

    def test_get_appshuoming(self):
        '''关于app'''
        self.url = self.host+'/api/comment/v2/regarding/app'
        self.token = xieru.rwenjian(self)
        data={
            'customerId':'975694035530285056',
            'token':self.token
        }

        self.r= requests.post(self.url,data=data)
        self.result = self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_appshuoming(self):
        '''h5 App的服务条款、隐私政策和Cookie策略说明'''
        self.url=self.host+'/api/comment/v2/regarding/policy/markup'
        self.token=xieru.rwenjian(self)
        '''cookie'''
        header = {
            'Access - Control - Allow - Origin': '*',
            'Access - Control - Allow - Credentials': 'true',
             'Access - Control - Expose - Headers': 'FooBar',
            'Content - Type': 'text / html',
            'charset' : 'utf - 8',
        }
        params={
            'callback': 'jQuery33106629296058094668_1523520851857',
            'policyName': 'cookieUsePolicy',
            '_': '1523523729131'
           # 'customerId': '975694035530285056',
            #'token': self.token
        }
        self.r=requests.get(self.url,params=params,headers=header)
        print(self.r.text)
        self.r2 = re.findall("{.*}", self.r)
        print(self.r2)
        #self.result=xieru.jiexi_jsonp(self.r)
        self.result=self.r2.json()
        self.assertEqual(self.result['code'], 0)
    def test_fuwu(self):
        self.url = self.host + '/api/comment/v2/regarding/policy/markup'
        self.token = xieru.rwenjian(self)
        '''服务'''
        params = {
            'callback': 'jQuery33106629296058094668_1523520851857',
            'policyName': 'TermsService',
            '_':'1523523729131'
            #'customerId': '975694035530285056',
            #'token': self.token
        }
        self.r2 = requests.get(self.url, patams=params)
        self.result2 = self.r2.json()
        self.assertEqual(self.result2['code'], 0)
    def test_yinsi(self):
        self.url = self.host + '/api/comment/v2/regarding/policy/markup'
        self.token = xieru.rwenjian(self)
        '''隐私'''
        data3 = {
            'callback': 'jQuery33106629296058094668_1523520851857',
            'policyName': 'PrivacyPolicy',
            '_': '1523523729131'
            #'customerId': '975694035530285056',
            #'token': self.token
        }
        self.r3 = requests.get(self.url, params=data3)
        self.result3 = self.r3.json()
        self.assertEqual(self.result3['code'], 0)



if __name__=='__main__':
    unittest.main()