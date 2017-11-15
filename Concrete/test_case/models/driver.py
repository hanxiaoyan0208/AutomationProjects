from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    # driver = webdriver.Chrome()
    host = '127.0.0.1:8080' # 运行主机：端口号
    dc = {'browserName':'chrome'} # 指定浏览器 （"chrome","firefox"）
    driver = Remote(command_executor='http://' + 'host' + '/concrete/a',desired_capabilities=dc)

    return driver
if __name__ =='__main__':
    dr = browser()
    dr.get("http://125.211.222.73:8080/concrete/a")
    dr.quit()