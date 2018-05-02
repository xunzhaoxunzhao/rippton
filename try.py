import unittest
from jiekou.fengzhuang.fangfa import *
import requests
from ddt import ddt
from jiekou.conf.env import *
import xlrd
import HTMLTestRunner
from xlutils.copy import copy
import time

class diyige(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        host=Host
        '''用户登入'''
        url = host + '/api/customer/v2/signin'
        password = xieru().mima()
        data = {
            'deviceToken': 'asdfghjkl',
            'deviceType': 'iphone',
            'email': '970404223@qq.com',
            'passwd':password
        }

        r = requests.post(url, data=data)

        result = r.json()
        token = result['data']['token']
        wenjian = open('C:/token/token.txt', 'w+')
        wenjian.write(token)
        wenjian.close()
        assert(result['code']==0)
    @classmethod
    def tearDownClass(cls):
        '''退出登入'''
        host = Host
        url = host + '/api/customer/v2/signout'
        token = xieru().rwenjian()
        data = {
            'customerId': '975694035530285056',
            'token':token
        }
        r = requests.post(url, data=data)
        result = r.json()
        assert (result['code'] == 0)


    def test_ReadExcel(self):
        self.host = Host
        results = []
        tishi=[]
        self.file = os.chdir('C:/Users/user01/Desktop')
        workbook = xlrd.open_workbook('apidemo.xls')
        sheet_name = workbook.sheet_by_index(0)
        self.token = xieru().rwenjian()
        nrow = sheet_name.nrows
        for i in range(1, nrow):
            url = self.host + sheet_name.cell_value(i, 1)
            requesttype = sheet_name.cell_value(i, 2)
            canshu = eval(sheet_name.cell_value(i, 3))
            self.yuqi = sheet_name.cell_value(i, 4)
            if requesttype == 'get':
                r = requests.get(url, params=canshu)
                result = r.json()
            elif requesttype == 'post':
                r = requests.post(url, data=canshu)
                result = r.json()
            elif requesttype == 'delete':
                r = requests.delete(url, data=canshu)
                result = r.json()
            if result['code'] == 0:
                results.append('True')
                tishi.append(result['msg'])
            else:
                results.append('False')
                tishi.append(result['msg'])

            r.close()
            print('共有%d个url，当前执行%d个' % ((nrow - 1), i))
        newwork = copy(workbook)
        sheet = newwork.get_sheet(0)
        for j in range(1, nrow):
            sheet.write(j, 5, results[j - 1])
            sheet.write(j,6,tishi[j - 1])
        os.remove('apidemo.xls')
        newwork.save('apidemo.xls')
        return results

if __name__=='__main__':
    testsuit = unittest.TestSuite()
    pathcode = 'C:/Users/user01/PycharmProjects/untitled/'
    testsuit.addTest(diyige('test_ReadExcel'))
    cuitime = time.strftime('%Y%m%d%H%M%S',time.localtime())
    HtmlFile =pathcode+cuitime+'.html'
    #HtmlFile = cuitime+'.html'
    #HtmlFile = 'result.html'
    fp =open(HtmlFile,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='接口测试报告',description='rippton')
    runner.run(testsuit)

    fp.close()