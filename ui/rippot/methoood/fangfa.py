from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
class dingwei(object):
    def find_xpath(self,text,xpath,zifu):
        if text=='click':
            return self.driver.find_element_by_xpath(xpath).click()
        elif text =='yuanshu':
            return self.driver.find_element_by_xpath(xpath)
        elif text=='sendkeys':
            return self.driver.find_element_by_xpath(xpath).send_keys(zifu)

    def duanyan(self,text,xpath,):
        '''
        if text == 'name':
            if self.driver.find_element_by_xpath(xpath).text == result:
                return True
            else:
                return False

         #   return self.assertEqual(self.driver.find_element_by_xpath(xpath).text,result)
        elif text == 'lujin':
            if self.driver.find_element_by_xpath(xpath).read() ==result:
                print(self.driver.find_element_by_xpath(xpath).text)
                return True
            else:
                print(self.driver.find_element_by_xpath(xpath).read())
                return False
           # return self.assertEqual(self.driver.find_element_by_xpath(xpath),result)
            '''
        if text =='lujin':

            cunzai = self.driver.find_element_by_xpath(xpath)
            #result =cunzai.is_enabled()
            result = cunzai.is_displayed()
            print(result)
            if result==True:
                return True
            else:
                return False
    def shuru(self,text,xapth,zifu):
        if text=='SR':
            return self.driver.find_element_by_xpath(xapth).send_keys(zifu)
        elif text=='huoqu':
            return self.driver.find_element_by_xpath(xapth).get_attribute(zifu)

    def get_toast(self,message):
        try:
            elemnt =WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.PARTIAL_LINK_TEXT,message))
            print(elemnt)
            return True
        except:
            return False

    '''
        抓取toast另一种方法
        var_toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % str_check_value)
        self.obj_el_or_els = WebDriverWait(self.obj_driver, num_timeout, num_wait_poll_frequency).until(
            expected_conditions.presence_of_element_located(var_toast_loc))
    '''


