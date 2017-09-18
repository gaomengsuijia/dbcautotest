#coding:utf-8
__author__ = "langtuteng"
from pageobj.loginpage import Loginpage
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






    def login_username(self,username):
        self.loginpage.findelment(*self.login_username_loc).send_keys(username)


    def login_password(self,password):
        self.loginpage.findelment(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.loginpage.findelment(*self.login_password_loc).click()


if __name__ == "__main__":
    driver = basedriver.Basedriver()
    pagelogin = Page_login(driver)
    # sleep(8)
    pagelogin.login_view()