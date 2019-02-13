from selenium import webdriver
import time


browser = webdriver.Chrome()
def login(name,pwd):
    browser.get( 'https://account.xiaomi.com/')#登录网址
    time.sleep(1)
    browser.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(1)
    browser.get("https://event.mi.com/tw/sales2018/super-sales-day")#切换到秒杀页面
    

def keepclick():
    while True:   #迴圈
        browser.find_element_by_xpath("//*[@id='sec_1']/div/div/ul/li/ol/li[4]/a/span").click()  #购买按钮的Xpath
        print("hit")
        

def main():
    login('你的帳號','你的帳號')
    keepclick()
    

if __name__ == '__main__':
    main()



 


