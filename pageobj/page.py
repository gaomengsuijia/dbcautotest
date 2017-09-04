#coding:utf-8
__author__ = "langtuteng"
from appium import webdriver

class Page(object):
    def __init__(self,desired_caps):
        self.driver =  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.desired_caps = desired_caps

    def __call__(self,desired_caps):
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        pass




    def find_elment(self,*args):
        return self.driver.find_elment(*args)


    def find_elments(self,*args):
        return self.driver.find_elments(*args)

