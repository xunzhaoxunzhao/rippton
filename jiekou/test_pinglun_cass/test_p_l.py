import unittest
import requests
from jiekou.fengzhuang.fangfa import *
import json

class test_ping(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.156.0.100:8080/rippton2nd'
    def tearDown(self):
        pass

    def test_fabiaopinglun(self):
     #   '''发表其他评论'''
        self.url = self.host+'/api/comment/v2/comment/do'
        self.token = xieru.rwenjian(self)
       # data = {
        #    'content':'1231313132',
         #   'customerId':'975694035530285056',
            #'isReply':'0',
          #  'itemId':'978910520088199168',
           # 'type':'4',
            #'token':self.token
        #}
        #self.r=requests.post(self.url,data=data)
        #self.result = self.r.json()
        #self.assertEqual(self.result['code'],0)
        '''发表鱼获评论'''
        data2 = {
            'content': '1231313132',
            'customerId': '975694035530285056',
            # 'isReply':'0',
            'itemId': '983903964380528640',
            'type': '1',
            'token': self.token
        }
        self.r2 = requests.post(self.url, data=data2)
        self.result2 = self.r2.json()
        self.assertEqual(self.result2['code'], 0)
        '''发表鱼探评论'''
        data3 = {
            'content': '1231313132',
            'customerId': '975694035530285056',
            # 'isReply':'0',
            'itemId': '983162733555875840',
            'type': '2',
            'token': self.token
        }
        self.r3 = requests.post(self.url, data=data3)
        #print(self.r3.text)
        self.result3 = self.r3.json()
        self.assertEqual(self.result3['code'], 0)
        '''发表经验评论'''
        data4 = {
            'content': '1231313132',
            'customerId': '975694035530285056',
            # 'isReply':'0',
            'itemId': '985784515047718912',
            'type': '3',
            'token': self.token
        }
        self.r4 = requests.post(self.url, data=data4)
        self.result4 = self.r4.json()
        self.assertEqual(self.result4['code'], 0)
        '''发表评论的评论'''
        data6 = {
            'content': '1231313132',
            'customerId': '975694035530285056',
             'isReply':'0',
            'itemId': '984032616288092160',
            'type': '6',
            'token': self.token
        }
        self.r6 = requests.post(self.url, data=data6)
        self.result6 = self.r6.json()
        self.assertEqual(self.result6['code'], 0)
       # '''发表活动评论'''
       #  'customerId': '975694035530285056',
            # 'isReply':'0',
       #     'itemId': '2c92808262b394630162b4988eee000f',
      #      'type': '5',
       #     'token': self.token,
       #     'score':'5.9'
      #  }
      #  self.r5 = requests.post(self.url, data=data5)
       # self.result5 = self.r5.json()
      # self.assertEqual(self.result5['code'], 0)

   # def test_chushipinglun(self):
      #  '''暂时不调用'''
       # self.url=self.host+'/api/comment/v2/comment/init'
        #self.token=xieru.rwenjian(self)
        #data = {
         #   'itemId': '984032399065088000',
          #  'rows':'15',
           # 'token':self.token,
           # 'page':'0'
        #}
        #self.r = requests.post(self.url,data=data)
        #self.result=self.r.json()
        #self.assertEqual(self.result['code'],0)
    def test_jiazaipinglun(self):
        '''加载时间点之前或之后的评论数据(最新数据)'''
        self.url = self.host+'/api/comment/v2/comment/list'
        self.token = xieru.rwenjian(self)
        data = {
            'customerId':'975694035530285056',
            'itemId':'984048299117903872',
            'lastest':'1',
            'rows':'15',
            'timeStamp':'-1',
            'token':self.token

        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
        '''加载时间点之前或之后的评论数据(历史数据)'''
        data2 = {
            'customerId': '975694035530285056',
            'itemId': '984048299117903872',
            'lastest': '0',
            'rows': '15',
            'timeStamp': '-1',
            'token': self.token

        }
        self.r2 = requests.post(self.url, data=data2)
        self.result2 = self.r2.json()
        self.assertEqual(self.result2['code'], 0)
    def test_shanchupinglun(self):
        '''删除我发的评论'''
        self.url = self.host+'/api/comment/v2/logical/delete'
        self.token =xieru.rwenjian(self)
        self.commenId=xieru.lianmysql(self)
        data = {
            'commentId':self.commenId,
            'customerId': '975694035530285056',
            'token':self.token
        }
        self.r = requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)

    def test_genjuidchaxunsuoyou(self):
        '''根据评论id查询所有回复的人id以及name'''
        self.url = self.host+'/api/comment/v2/subcomment/customer'
        self.token=xieru.rwenjian(self)
        self.commenId=xieru.lianmysql(self)
        data={
            'commentId':self.commenId,
            'token':self.token,
             'customerId': '975694035530285056',
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
    def test_yonghufankui(self):
        '''用户反馈'''
        self.url=self.host+'/api/comment/v2/suggestion'
        self.token=xieru.rwenjian(self)
        data = {
            'content':'测试测试',
            'customerId':'975694035530285056',
            'token':self.token
        }
        self.r=requests.post(self.url,data=data)
        self.result=self.r.json()
        self.assertEqual(self.result['code'],0)
if __name__=='__mian__':
    unittest.main()