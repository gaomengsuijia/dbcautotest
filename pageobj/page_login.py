#coding:utf-8
__author__ = "langtuteng"
from pageobj.loginelment import Loginpage
from appium.webdriver.common.mobileby import By
from driverbase import basedriver
from time import sleep
class Page_login():


    def __init__(self,driver):
        self.loginpage = Loginpage(driver)


    def login_view(self):
        self.loginpage.go_login_page()
        # print(self.driver.get_activity())
        # if self.driver.get_activity() == '.DbcMainActivity':
        #     print('ok')
        #     myelemnt = self.driver.findelment(*self.login_maintab_loc)
        #     print(myelemnt)
        #     myelemnt.click()
        #     print('ok')

    def go_logon(self):
        self.loginpage.find_gologin().click()

    def send_username(self,username):
        self.loginpage.find_username_el().send_keys(username)


    def send_password(self,password):
        self.loginpage.find_password_el().send_keys(password)

    def send_code(self,code):
        self.loginpage.find_code_el().send_keys(code)

    def login_button(self):
        self.loginpage.find_login_el().click()


if __name__ == "__main__":
    driver = basedriver.Basedriver()
    pagelogin = Page_login(driver)
    # sleep(8)
    pagelogin.send_username('18565660212')
    pagelogin.send_password('123456')