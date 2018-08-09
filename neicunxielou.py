import os
import re
from xlwt import Workbook
from xlutils.copy import copy
zhushuju = []
hushuju=[]
def shebei():
    chaxun=os.popen('adb devices').read()
    pi = re.compile('\n.*?(device)', re.S)
    try:
        pei=re.findall(pi,chaxun)[0]
    except:
        pei='game over'
        print('已断开')
    return pei
def baoming():
    print('拔掉数据线或断开设备连接即表示任务结束,任务结束后程序会自动关闭，数据存储C:/Users/user01/Desktop目录中的内存泄露.xls')
    print('开始查找包名，请进入相应的应用')
    input('已进入应用请输入ok>>>>>>>>>>>>>')
    BM=os.popen('adb shell dumpsys window | findstr mCurrentFocus').read()
   # print(BM)
    bm=re.compile('(com.*?)/',re.S)
    try:
        fanhuibaoming=re.findall(bm,BM)[0]
    except:
        print('未连接')
   # print(fanhuibaoming)
    def neicun():
        try:
            os.chdir(r'C:\Users\user01\Desktop')
        except:
            os.makedirs(r'C:\Users\user01\Desktop')
            os.chdir(r'C:\Users\user01\Desktop')
        # mingcheng=time.time()
        # shujubiaoge = 'sj' + '%s' % mingcheng
        shujubiaoge = Workbook(encoding='utf-8')
        sheet1=shujubiaoge.add_sheet('内存泄露数据')

        while True:
            try:
                zhi=os.popen('adb shell dumpsys meminfo |findstr %s'%fanhuibaoming).read()
            except:
                pass
            #print(zhi)
            dashuzi=re.compile('( .*?)K.*?\n(.*?)K',re.S)
            fujingchengming=re.compile(': (.*?) ',re.S)
            try:
                a=re.findall(dashuzi,zhi)[0]
                a=list(a)
                for i in range(len(a)):
                    a[i]=a[i].replace(' ','')
                    a[i]=round(int(a[i].replace(',',''))/1024,2)
               # print(a[i])
                    if i==0:
                        zhushuju.append(a[i])
                    elif (i % 2)==0:
                        zhushuju.append(a[i])
                    else:
                        hushuju.append(a[i])
            except:
                pass
            try:
                d=re.findall(fujingchengming,zhi)
            except:
                pass
            # jinc=[]
            # for i in range(2):
            #     #print(d[i])
            #     jinc.append(d[i])
            #     #sheet1.write(0,i,d[i])
            #     # print(a,d)

            if shebei()=='device':
                pass
            else:
                break
        try:
            sheet1.write(0, 0, d[0])
            sheet1.write(0, 1, d[1])
        except:
            pass
        try:
            for b in range(len(zhushuju)):
                sheet1.write(b+1,0,zhushuju[b])
            for c in range(len(hushuju)):
                sheet1.write(c+1,1,hushuju[c])
        except:
            pass
        try:
            shujubiaoge.save('内存泄露.xls')
        except:
            newwork=copy(shujubiaoge)
            sheet = newwork.get_sheet(0)
            try:
                sheet.write(0, 0, d[0])
                sheet.write(0, 1, d[1])
                for b in range(len(zhushuju)):
                    sheet.write(b+1,0,zhushuju[b])
                for c in range(len(hushuju)):
                    sheet.write(c+1,1,hushuju[c])
                os.remove('内存泄露.xls')
                newwork.save('内存泄露.xls')
            except:
                print('保存失败/已有同文件')
    return neicun()



if __name__=='__main__':
    while 1:
        shebei()
        baoming()