from appium import webdriver
import os
import time
def start_app():
 #   cmd ='appium -a 127.0.0.1 -p 4723'
   # __appium=os.popen(cmd)
   # print(__appium.read())
   # time.sleep(5)
    des_caps = {}
    des_caps['platformName']='Android'
    '''SANNXING'''
    des_caps['deviceName']='ce0817187528b83a047e'
    '''LG'''
    #des_caps['deviceName']='LGAS993c50b2570'
    des_caps['platformVersion']='7.1.1'
    des_caps['appPackage']='com.zhongke.rippton'
    des_caps['appActivity']='com.zhongke.rippton.MainActivity'
    des_caps['unicodeKeyboard']=True
    des_caps['resetKeyboard']=True
    des_caps['noReset']='true'
    #des_caps['automationName']='Uiautomator2'
   # des_caps['newCommandTimeout'] = '300'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des_caps)
    return driver