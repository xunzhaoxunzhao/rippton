import unittest
import xlrd
from xlutils.copy import copy
import time
import os
from ui.rippot.methoood.fangfa import *
from ui.rippot.qidong.qidongyuansu import *
results = []
class READ(unittest.TestCase):
    def setUp(self):
        self.driver = start_app()
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()

    def test_excel(self):
        self.file = os.chdir('C:/Users/user01/Desktop')
        workbook = xlrd.open_workbook('UI.xls')
        sheet_name = workbook.sheet_by_index(0)
        norw = sheet_name.nrows
        for i in range(1,norw):
            text = sheet_name.cell_value(i,2)
           # print(text)
            xpath = sheet_name.cell_value(i,3)
          #  print(xpath)
            zifu = sheet_name.cell_value(i,4)
           # print(zifu)
           # result = sheet_name.cell_value(i,5)
            dingwei.find_xpath(self,text,xpath,zifu)
           # dingwei.duanyan(self,text,xpath,result)
           # jieguo=dingwei.duanyan(self,text,xpath,result)
            #jieguo=duanyuan(text,xpath,result)
           # print(jieguo)
            jieguo = dingwei.duanyan(self,text,xpath)
            results.append(jieguo)
        #print(results)
        newwork = copy(workbook)
        sheet =newwork.get_sheet(0)
        for j in range(1,norw):
            sheet.write(j,5,results[j-1])
        os.remove('UI.xls')
        newwork.save('UI.xls')
        return results

if __name__=='__main__':
    unittest.main()