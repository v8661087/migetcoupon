from selenium import webdriver
import time


browser = webdriver.Chrome()
def login(name,pwd):
    browser.get( 'https://account.xiaomi.com/')#登錄網址
    time.sleep(1)
    browser.find_element_by_id("username").send_keys(name) #利用帳號標籤的ID，確定位置並send信息
    browser.find_element_by_id("pwd").send_keys(pwd) #利用密碼標籤的ID，確定位置並send信息
    browser.find_element_by_id("login-button").click()#利用登錄按鈕的ID，確定位置並點擊
    #如果找不到標籤ID，可以使用其他方法來確定元素位置
    time.sleep(1)
    browser.get("https://event.mi.com/tw/sales2018/super-sales-day")#切換到頁面
    

def keepclick():
    while True:   #迴圈
        browser.find_element_by_xpath("//*[@id='sec_1']/div/div/ul/li/ol/li[4]/a/span").click()  #按鈕的Xpath
        print("hit")
        

def main():
    login('name','pwd') #name為你的帳號，pwd為你的密碼
    keepclick()
    

if __name__ == '__main__':
    main()



 


