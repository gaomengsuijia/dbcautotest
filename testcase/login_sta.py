#coding:utf-8
__author__ = "langtuteng"

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import unittest
from pageobj.page_login import Page_login
from bin.mycaps import mycaps
import time

class Test_login(unittest.TestCase):
    '''
    test login
    '''

    def setUp(self):
        print("test login begin")


    def tearDown(self):
        print("test login end")

    @classmethod
    def setUpClass(cls):
        print("start only once")

    @classmethod
    def tearDownClass(cls):
        print("end only once")


    def user_login_verify(self,username='',password=''):
        desired_caps = mycaps('Android', '4.4.2', '6248724d', 'true', 'com.ap.dbc.app','com.ap.dbc.app.SplashActivity')
        pagelogin = Page_login(desired_caps)
        time.sleep(8)
        pagelogin.login_view()
        time.sleep(2)
        pagelogin.login_username(username)
        time.sleep(2)
        pagelogin.login_password(password)
        time.sleep(2)
        pagelogin.login_button()




    def login_success(self):
        '''
        用户名正确
        密码正确
        :return:
        '''
        self.user_login_verify(username='18565660212',password='123456')
        print("login_success")

    def login_fail(self):
        '''
        用户名正确
        密码错误
        :return:
        '''
        self.user_login_verify(username='18565660212',password='654321')
        print("login_fail")



if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Test_login('login_success'))
    suit.addTest(Test_login('login_fail'))
    unittest.TextTestRunner().run(suit)
