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
        print(desired_caps_conf)

        return driver

    def close(self):
        self.driver.close()


if __name__=="__main__":
    drive = Basedriver()
    print(drive)