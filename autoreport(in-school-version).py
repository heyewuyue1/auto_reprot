from selenium import webdriver
# TODO 文件存储所有用户的账号密码

'''
登录页面网址：https://app.bupt.edu.cn/ncov/wap/default/index
'''
 
driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')

def login(id:str, password:str)->int:
    driver.get("https://app.bupt.edu.cn/ncov/wap/default/index")
