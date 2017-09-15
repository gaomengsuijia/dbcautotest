#coding:utf-8
__author__ = "langtuteng"
from pageobj.page import Page
from appium.webdriver.common.mobileby import By
from driverbase import basedriver
from time import sleep
class Page_login(Page):


    #action

    login_username_loc = (By.ID,"com.ap.dbc.app:id/et_login_phone")
    login_password_loc = (By.ID,"com.ap.dbc.app:id/et_login_psw")
    login_button_loc = (By.ID,"com.ap.dbc.app:id/bt_login")
    login_maintab_loc = (By.ID,"com.ap.dbc.app:id/main_tab_profile_tv")
    login_head_loc = (By.ID,"com.ap.dbc.app:id/iv_default_heading")

    def __init__(self,driver):
        self.driver = Page(driver)


    def login_view(self):
        self.driver.wait()
        print(self.driver.get_activity())
        if self.driver.get_activity() == '.DbcMainActivity':
            print('ok')
            myelemnt = self.driver.findelment(*self.login_maintab_loc)
            print(myelemnt)
            myelemnt.click()
            print('ok')



    def login_username(self,username):
        self.driver.findelment(*self.login_username_loc).send_keys(username)


    def login_password(self,password):
        self.driver.findelment(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.driver.findelment(*self.login_password_loc).click()


if __name__ == "__main__":
    driver = basedriver.Basedriver()
    pagelogin = Page_login(driver)
    # sleep(8)
    pagelogin.go_login_page()
    pagelogin.login_view()