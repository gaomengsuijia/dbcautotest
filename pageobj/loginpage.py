#coding:utf-8
__author__ = "langtuteng"
from driverbase import basedriver
from time import sleep
from appium.webdriver.common.mobileby import By
from selenium.common.exceptions import NoSuchElementException,WebDriverException
class Loginpage(object):
    per_loc = (By.ID,'android:id/button1')
    def __init__(self,driver):
        self.driver =  driver

    def __call__(self):
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        pass

    #
    # def swip(self,*args):
    #      self.driver.myswipe(*args)


    # def get_wind_sz(self):
    #     return self.driver.get_wind_size()


    def swipe_left(self,t=1000):
        '''
        向左滑动
        :return:
        '''
        l = self.driver.get_wind_size()
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.driver.myswipe(x1,y1,x2,y1,t)


    def swipe_right(self,t=1000):
        '''
        向右滑动
        @t 滑动时间
        :return:
        '''
        l = self.driver.get_wind_size()
        x1 = int(l[0]*0.25)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.75)
        self.driver.myswipe(x1,y1,x2,y1,t)

    def swipe_top(self,t=1000):
        '''
        向上滑动
        :param t:
        :return:
        '''
        l = self.driver.get_wind_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[1] * 0.9)
        self.driver.myswipe(x1, y1, x1, y2, t)

    def swipe_bottom(self,t=1000):
        '''
        向下滑动
        :param t:
        :return:
        '''
        l = l = self.driver.get_wind_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.1)
        self.driver.myswipe(x1, y1, x1, y2, t)

    def get_per(self):
        try:
            per = self.driver.findelment(*self.per_loc)
            per.click()
        except NoSuchElementException as e:
            print("找不到元素")


    # def tap_screen(self,position,duration):
    #     self.driver.mytap(position,duration)


    def go_login_page(self):
        for i in range(4):
            print('开始滑动%s' % str(i))
            self.swipe_left(t=1000)
        sleep(4)
        # 处理权限弹出窗口
        self.get_per()
        self.get_per()

        # 处理新手引导
        self.driver.mytap([(500, 500)], 500)



if __name__ == "__main__":
    driver = basedriver.Basedriver()
    loginpage = Loginpage(driver)
    sleep(2)
    loginpage.go_login_page()




