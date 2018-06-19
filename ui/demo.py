from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
fast_url='https://www.baidu.com'
print('now url is %s'%fast_url)
driver.get(url=fast_url)
time.sleep(3)
a="D:\\test\\ont.png"
driver.get_screenshot_as_file(a)
driver.find_element_by_id('kw').send_keys('selenium')
#time.sleep(2)
driver.find_element_by_xpath("//input[@id='su']").submit()
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()

#driver.find_elements_by_class_name('_fzTWq').click()
print('back to %s'%fast_url)
driver.back()
print(driver.title)
driver.find_element_by_link_text('贴吧').click()
print(driver.title)
driver.find_element_by_xpath("//*[@id='wd1']").send_keys('rng')
driver.find_element_by_xpath("//input[@name='kw1']").send_keys(Keys.ENTER)
driver.get_screenshot_as_file(a)
a=driver.find_element_by_xpath("//*[@id='thread_list']/li[2]/div/div[2]/div[1]/div[1]")
b=a.title
driver.back()
time.sleep(1)
driver.back()
print(driver.title)
driver.find_element_by_tag_name('input').send_keys(Keys.CONTROL,'v')
#driver.find_elements_by_class_name('t c-gap-bottom-small').click()
#driver.find_element_by_xpath("//h3[@class='t c-gap-bottom-small']").click()
#driver.quit()