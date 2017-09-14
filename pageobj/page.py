#coding:utf-8
__author__ = "langtuteng"
from driverbase import basedriver
from time import sleep
class Page(object):
    def __init__(self,driver):
        self.driver =  driver

    def __call__(self):
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        pass


    def swip(self,*args):
        return self.driver.myswipe(*args)


    def get_wind_sz(self):
        return self.driver.get_wind_size()


    def swipe_left(self,t):
        '''
        向左滑动
        :return:
        '''
        l = l = self.get_wind_sz()
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.swip(x1,y1,x2,y1,t)


    def swipe_right(self,t):
        '''
        向右滑动
        @t 滑动时间
        :return:
        '''
        l = self.driver.get_wind_sz()
        x1 = int(l[0]*0.25)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.75)
        self.swip(x1,y1,x2,y1,t)

    def swipe_top(self,t):
        '''
        向上滑动
        :param t:
        :return:
        '''
        l = self.driver.get_wind_sz()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[1] * 0.9)
        self.swip(x1, y1, x1, y2, t)

    def swipe_bottom(self,t):
        '''
        向下滑动
        :param t:
        :return:
        '''
        l = l = self.driver.get_wind_sz()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.1)
        self.swip(x1, y1, x1, y2, t)



if __name__ == "__main__":
    driver = basedriver.Basedriver()
    page = Page(driver)
    sleep(5)
    print(page.get_wind_sz())
    for i in range(2):
        page.swipe_left(1)


