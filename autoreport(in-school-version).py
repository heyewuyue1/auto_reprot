from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
# TODO 定位功能有问题

# 设置一些常量

# 设置网络驱动器，火狐浏览器，无界面
option = webdriver.FirefoxOptions()
option.add_argument('--headless')
driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')

# 登录界面地址
login_page_url = r"https://app.bupt.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex"

# 填报页面地址
form_url = "https://app.bupt.edu.cn/ncov/wap/default/index"

# 帐号输入框xpath
id_input = "/html/body/div[1]/div[2]/div[1]/input"

# 密码输入框xpath
password_input = "/html/body/div[1]/div[2]/div[2]/input"

# 登录按钮
login_button = "/html/body/div[1]/div[3]"

# 今日是否在校按钮
inschool_button_yes = "/html/body/div[1]/div/div/section/div[4]/ul/li[4]/div/div/div[1]/span[1]/i"
inschool_button_no = "/html/body/div[1]/div/div/section/div[4]/ul/li[4]/div/div/div[2]/span[1]/i"
inschool_button_confirm = "/html/body/div[3]/div/div[2]/div[2]"

# 定位
location_button = "/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div/input"

# 中高风险地区
high_risk_area_button = "/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div/div/div[2]/span[1]/i"

# 提交按钮
submitt_button = "/html/body/div[1]/div/div/section/div[5]/div/a"

# 用户类
class user:

    # 用户的学号
    user_id: str

    #用户的密码
    user_password: str

    #用户在管理系统中的索引
    user_index: int

    #构造函数 
    def __init__(self, user_id:str, user_password:str)->None:
        self.user_id = user_id
        self.user_password = user_password


    def login(self)->bool:
        print("用户：" + self.user_id +" 正在登录...")
        try:
            driver.get(login_page_url)  # 打开登录界面
            driver.implicitly_wait(15)
            driver.find_element_by_xpath(id_input).send_keys(self.user_id)              # 输入学号
            driver.find_element_by_xpath(password_input).send_keys(self.user_password)  # 输入密码
        except:
            print("无法打开登录页面\n")

        driver.find_element_by_xpath(login_button).click()  # 点击登录按钮
        sleep(3)    # 等待页面加载

        if driver.current_url == form_url:
            print("用户：" + self.user_id +" 登录成功！")
            return True
        else:
            print("用户：" + self.user_id +" 登录失败，请检查学号密码是否正确（默认密码为身份证号后6位）")
            return False

    def fill_form(self)->bool:
        print("用户：" + self.user_id +" 正在填报...")
        driver.find_element_by_xpath(inschool_button_yes).click()     # 点击是否在校->是
        sleep(0.5)
        try:
            driver.find_element_by_xpath(inschool_button_confirm).click()# 点击确认按钮
        except NoSuchElementException:
            print("不需要确认在校")
        # driver.find_element_by_xpath(location_button).click()   # 点击定位按钮
        # sleep(5)
        driver.find_element_by_xpath(high_risk_area_button).click() # 点击是否在中高风险地区->否
        sleep(0.5)
        driver.find_element_by_xpath(submitt_button).click()    # 点击提交按钮
        return True

    def report(self)->bool:
        is_login = self.login()
        is_fill_form = self.fill_form()

        if is_login and is_fill_form:
            print("用户：" + self.user_id +" 填报完成！")
            return True
        else:
            print("用户：" + self.user_id +" 填报失败！")
            return False

def main():
    hjh = user("2020211435", "10070016")
    hjh.report()



if __name__ == "__main__":
    main()
