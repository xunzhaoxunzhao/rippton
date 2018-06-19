from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui.rippot.evn.cogfin import *
from ui.rippot.qidong.qidongyuansu import *
import time
import unittest
from ui.rippot.methoood.fangfa import *
class dengru(unittest.TestCase):
    def setUp(self):

        self.driver =start_app()
        time.sleep(3)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
    def test_dengrutishi(self):
        dingwei.shuru(self,'SR',DR['账号'],sendkeys['账号'])
        dingwei.shuru(self,'SR',DR['密码'],sendkeys['错误的密码'])
        dingwei.find_xpath(self,'click',DR['登入'])
        time.sleep(2)
        dingwei.get_toast(self,'Account or password is incorrect')
    def test_shuruzhanghaomima(self):
       dingwei.shuru(self,'SR',DR['账号'],sendkeys['账号'])
       dingwei.shuru(self,text='SR',xapth=DR['密码'],zifu=sendkeys['密码'])
       #dingwei.find_xpath('click',DR['明密文'])
       time.sleep(3)
       t=dingwei.shuru(self,text='huoqu',xapth=DR['密码'],zifu=sendkeys['passwd'])
       if t=='true':
           dingwei.find_xpath(self,text='click',xpath=DR['明密文'])
       else:
           pass
       m = dingwei.shuru(self, text='huoqu', xapth=DR['密码'], zifu=sendkeys['passwd'])
       print(m)
       a= self.assertEqual(m,'false')
       print(a)
       dingwei.find_xpath('click',DR['登入'])

if __name__=='__main__':
    unittest.main()