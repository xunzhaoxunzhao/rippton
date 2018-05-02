import os
import pymysql as mdb
import time
import re
import json
import base64
import hashlib
_jsonp_begin = r'callback('
_jsonp_end = r')'
import json
class xieru(object):

    def rwenjian(self):
        '''token'''
        self.read = open('C:/token/token.txt', 'r')
        self.Read = self.read.readline()
        #print(self.Read)
        self.read.close()
       # print(self.Read)
        return self.Read

    def xianzufangfaming(self):
        '''时间'''
        time_now =int(time.time())
        return time_now

    def lianmysql(self):
        config={
            'host':'10.156.0.102',
            'port':3306,
            'user':'root',
            'passwd':'drone123456',
            'db':'aerialvehicle',
            'charset':'utf8'
        }
        self.conn = mdb.connect(**config)
        self.cur = self.conn.cursor()
        self.countId=self.cur.execute("select id from tbl_comment where create_name='x l' and item_id='983903964380528640'")
        #self.result = self.cur.fetchone()
        self.results = self.cur.fetchall()
        for self.resul in self.results:
            self.result=self.resul[-1]
            #print(self.result)
        self.cur.close()
        self.conn.close()
        return self.result


    def lianmysql_shegnhuoid(self):
        config={
            'host':'10.156.0.102',
            'port':3306,
            'user':'root',
            'passwd':'drone123456',
            'db':'aerialvehicle',
            'charset':'utf8'
        }
        self.conn = mdb.connect(**config)
        self.cur = self.conn.cursor()
        self.countId=self.cur.execute("select id from tbl_distribution_other where customer_id='975694035530285056';")
        #self.result = self.cur.fetchone()
        self.results = self.cur.fetchall()
        for self.resul in self.results:
            self.result=self.resul[-1]
            #print(self.result)
        self.cur.close()
        self.conn.close()
        return self.result
    def lianmysql_yuhuoid(self):
        config={
            'host':'10.156.0.102',
            'port':3306,
            'user':'root',
            'passwd':'drone123456',
            'db':'aerialvehicle',
            'charset':'utf8'
        }
        self.conn = mdb.connect(**config)
        self.cur = self.conn.cursor()
        self.countId=self.cur.execute("select id from tbl_catches where customer_id='975694035530285056' ORDER BY create_date;")
        #self.result = self.cur.fetchone()
        self.results = self.cur.fetchall()
        for self.resul in self.results:
            self.result=self.resul[-1]
            #print(self.result)
        self.cur.close()
        self.conn.close()
        return self.result

    def lianmysql_jingyanid(self):
        config={
            'host':'10.156.0.102',
            'port':3306,
            'user':'root',
            'passwd':'drone123456',
            'db':'aerialvehicle',
            'charset':'utf8'
        }
        self.conn = mdb.connect(**config)
        self.cur = self.conn.cursor()
        self.countId=self.cur.execute("select create_name from tbl_catches where customer_id='975694035530285056' ORDER BY create_date;")
        #self.result = self.cur.fetchone()
        self.results = self.cur.fetchall()
        for self.resul in self.results:
            self.result=self.resul[-1]
        #print(self.result)
        self.jyid=self.cur.execute("select id from tbl_sea_fishing_experience where create_name='%s' ORDER BY create_date;" %self.result)
        self.jiyans=self.cur.fetchall()
        for self.jiyan in self.jiyans:
            self.zuihouyige =self.jiyan[-1]
        self.cur.close()
        self.conn.close()
        #print(self.zuihouyige)
        return self.zuihouyige



    def jiexi_jsonp(self):
        self.JSONP = 'callbackFunction(["customername1","customername2"])'
        self.j = json.loads(re.findall(r'^\w+\((.*)\)$', self.JSONP)(int[0]))
       # print(type(self.j), self.j)
        return self.j



    def lianmysql_tandian(self):
        config={
            'host':'10.156.0.102',
            'port':3306,
            'user':'root',
            'passwd':'drone123456',
            'db':'aerialvehicle',
            'charset':'utf8'
        }
        self.conn = mdb.connect(**config)
        self.cur = self.conn.cursor()
        self.countId=self.cur.execute("select id from tbl_fishing_spots where customer_id='975694035530285056' ORDER BY create_date;")
        #self.result = self.cur.fetchone()
        self.results = self.cur.fetchall()
        for self.resul in self.results:
            self.result=self.resul[-1]
            #print(self.result)
        self.cur.close()
        self.conn.close()
        return self.result

    def zhuanmatupian(self):
        with open(r'C:/鱼照/3.jpg','rb') as f:
            ls = base64.b64encode(f.read())
            jiexi = str(ls,'utf-8')
        f.close()
        return jiexi


    def mima(self):
        a = '123456'
        m = hashlib.md5()
        m.update(a.encode('utf-8'))
        pwd = m.hexdigest()

        return pwd