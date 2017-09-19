#coding:utf-8
__author__ = "langtuteng"
from time import sleep
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from pageobj.loginhandle import Loginhandle
from driverbase.basedriver import Basedriver
import HTMLTestRunner

class Test_login(unittest.TestCase):
    '''
    test login
    '''

    def setUp(self):
        print("test login begin")
        self.driver = Basedriver()
        sleep(3)
        self.loginhandle = Loginhandle(self.driver)



    def tearDown(self):
        print("test login end")
        self.driver.closed()

    @classmethod
    def setUpClass(cls):
        print("start only once")


    @classmethod
    def tearDownClass(cls):
        print("end only once")



    def login_success(self):
        '''
        用户名正确
        密码正确
        :return:
        '''
        self.loginhandle.login('123456','18565660212')
        print("login_success")

    def login_fail(self):
        '''
        用户名正确
        密码错误
        :return:
        '''
        self.loginhandle.login('123455', '18565660212')
        print("login_fail")



if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Test_login('login_success'))
    suit.addTest(Test_login('login_fail'))
    unittest.TextTestRunner().run(suit)
