#coding:utf-8
__author__ = "langtuteng"
from pageobj.page import Page
from appium.webdriver.common.mobileby import By
class Page_login(Page):

    #action

    login_username_loc = (By.ID,"com.ap.dbc.app:id/et_login_phone")
    login_password_loc = (By.ID,"com.ap.dbc.app:id/et_login_psw")
    login_button_loc = (By.ID,"com.ap.dbc.app:id/bt_login")
    login_maintab_loc = (By.ID,"com.ap.dbc.app:id/main_tab_profile_layout")
    login_head_loc = (By.ID,"com.ap.dbc.app:id/iv_default_heading")

    def login_view(self):
        self.find_elment(*self.login_maintab_loc).click()
        self.find_elment(*self.login_head_loc).click()


    def login_username(self,username):
        self.find_elment(*self.login_username_loc).send_keys(username)


    def login_password(self,password):
        self.find_elment(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_elment(*self.login_password_loc).click()
