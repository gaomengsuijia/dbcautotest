#coding:utf-8
__author__ = "langtuteng"
from pageobj.page_login import Page_login
from driverbase.basedriver import Basedriver
from time import sleep


class Loginhandle(object):
    '''
    统一的登录入口
    '''

    def __init__(self,driver):
        self.loginpage = Page_login(driver)


    def login(self,password,username):
        '''
        登录
        :param password:
        :param username:
        :return:
        '''
        self.loginpage.go_logon()
        self.loginpage.send_username(username=username)
        self.loginpage.send_password(password=password)
        self.loginpage.login_button()


if __name__ == "__main__":
    driver = Basedriver()
    sleep(3)
    loginhandle = Loginhandle(driver)
    loginhandle.login('123456','18565660212')