from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

#    ============定义发送邮件===========
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("hanxiaoyan0208@163.com","hanHAN0621") #邮箱账号+密码
    smtp.sendmail("hanxiaoyan0208@163.com","1194229937@qq.com",msg.as_string())
    smtp.quit()
    print ('email has send out!')

#   =============查找测试报告目录，找到最新生成的测试报告文件============
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = '..\\Concrete\\report\\' + now + 'result.html'
    #print(os.getcwd())
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='魅族社区自动化测试报告',
                            description='环境：windows 7 浏览器：chrome')
    discover = unittest.defaultTestLoader.discover('..\\Concrete\\test_case',
                                                   pattern='*_sta.py')
    runner.run(discover)
    fp.close()  #关闭生成的报告
    file_path = new_report('..\\Concrete\\report\\')    #查找新生成的报告
    send_mail(file_path)    #调用发邮件模块