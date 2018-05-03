import unittest
from jiekou.fengzhuang.fangfa import *
import requests
from ddt import ddt
from jiekou.conf.env import *
import xlrd
import HTMLTestRunner
from xlutils.copy import copy
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

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
        self.jingyabn = xieru.lianmysql_jingyanid(self)
        self.tupian = xieru.zhuanmatupian(self)
        self.commenId = xieru.lianmysql(self)
        self.shegnhuo = xieru.lianmysql_shegnhuoid(self)
        self.shijan = xieru.xianzufangfaming(self)
        self.yuhuoid = xieru.lianmysql_yuhuoid(self)
        self.tupian = xieru.zhuanmatupian(self)
        self.neme = xieru.xianzufangfaming(self)
        self.name = str(self.neme) + 'a'
        self.mingzi = xieru.xianzufangfaming(self)
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
            print('共有%d个url，当前执行%d个' % ((nrow - 1),i))
        newwork = copy(workbook)
        sheet = newwork.get_sheet(0)
        for j in range(1, nrow):
            sheet.write(j, 5, results[j - 1])
            sheet.write(j,6,tishi[j - 1])
        os.remove('apidemo.xls')
        newwork.save('apidemo.xls')
        return results
    def test_mail(self):
        username = '970404223@qq.com'
        password = 'zlzrqcroorrobcgj'
        sender = username
        receivers = ','.join(['970404223@qq.com'])
        # receivers =['1301868201@qq.com']
        msg = MIMEMultipart()
        msg['Subject'] = 'shenghuidai Test'
        msg['From'] = sender
        msg['To'] = receivers

        # 下面是文字部分，也就是纯文本
        puretext = MIMEText('测试报告')
        msg.attach(puretext)

        # 定义附件的类型
        xlsxpart = MIMEApplication(open('C:/Users/user01/Desktop/apidemo.xls', 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename='apidemo.xls')
        msg.attach(xlsxpart)

        try:
            client = smtplib.SMTP_SSL('smtp.qq.com', 465)
            client.login(username, password)
            client.sendmail(sender, receivers, msg.as_string())
            client.quit()
            # print (f'带有附件{name}的邮件发送成功！')

        except:
            print('邮件发送失败')


if __name__=='__main__':
    testsuit = unittest.TestSuite()
    pathcode = 'C:/Users/user01/PycharmProjects/untitled/'
    testsuit.addTest(diyige('test_ReadExcel'))
    testsuit.addTest(diyige('test_mail'))
    cuitime = time.strftime('%Y%m%d%H%M%S',time.localtime())
    HtmlFile =pathcode+cuitime+'.html'
    #HtmlFile = cuitime+'.html'
    #HtmlFile = 'result.html'
    fp =open(HtmlFile,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='接口测试报告',description='rippton')
    runner.run(testsuit)
    fp.close()
