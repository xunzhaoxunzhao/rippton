from appium import webdriver
import time
des_caps = {
    'platformName':'Android',
    'deviceName':'3HX0217616001124',
    'platformVersion':'8.0.0',
    'appPackage':'com.zhongke.rippton',
    'appActivity':'com.zhongke.rippton.MainActivity',
    'unicodeKeyboard':True,
    'resetKeyboard':True,
    'noReset':True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des_caps)
time.sleep(1)
driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText[1]").send_keys('970404223@qq.com')
driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText[1]").send_keys("123456")

t= driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]").get_attribute("password")
print(t)