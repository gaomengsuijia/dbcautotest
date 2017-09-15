#coding:utf-8
__author__ = "langtuteng"
from utils import readconfig
from appium import webdriver
from time import sleep
class Basedriver(object):

    def __init__(self):
        '''
        返回dirver
        '''
        self.driver = self.basedriver()



    def basedriver(self):
        '''
        读取配置文件，返回dirver
        :return:
        '''
        desired_caps_conf = readconfig.readconfig()
        sleep(2)
        desired_caps = {}
        desired_caps['platformName'] = desired_caps_conf['platformName']
        desired_caps['platformVersion'] = desired_caps_conf['platformVersion']
        desired_caps['deviceName'] = desired_caps_conf['deviceName']
        desired_caps['autoLaunch'] = desired_caps_conf['autoLaunch']
        # desired_caps['app'] = conf.PATH
        desired_caps['appPackage'] = desired_caps_conf['appPackage']
        # desired_caps['appActivity'] = '.ui.activity.LoginActivity'
        desired_caps['appActivity'] = desired_caps_conf['appActivity']
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # print(desired_caps_conf)

        return driver

    def findelment(self,*args):
        return self.driver.find_element(*args)


    def findelments(self,*args):
        return self.driver.find_elements(*args)


    def myswipe(self,*args):
        '''
        滑动屏幕
        :param args:
        :return:
        '''
        print(args)
        self.driver.swipe(*args)
        print("滑动完成")

    def mytap(self,*args):
        '''
        点击屏幕
        :param args:
        :return:
        '''
        self.driver.tap(*args)



    def get_wind_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print(x,y)
        return (x,y)

    def wait(self,time=10):
        self.driver.implicitly_wait(time)


    def close(self):
        self.driver.close()

    def get_activity(self):
        '''
        返回当前的activity
        :return:
        '''
        return self.driver.current_activity



if __name__=="__main__":
    drive = Basedriver()
    print(drive.driver)