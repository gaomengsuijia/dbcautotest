#coding:utf-8
__author__ = "langtuteng"
from driverbase import basedriver

class Page(object):
    def __init__(self):
        self.driver =  basedriver.Basedriver()

    def __call__(self):
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        pass


    def find_elment(self,*args):
        return self.driver.find_elment(*args)


    def find_elments(self,*args):
        return self.driver.find_elments(*args)


    def get_wind_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)

    def swipt_left(self,t):
        '''
        向左滑动
        :return:
        '''
        l = self.get_wind_size()
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.9)
        x2 = int(l[0]*0.1)
        self.driver.swipt(x1,y1,x2,y1,t)


if __name__ == "__main__":
    page = Page()
    print(page.get_wind_size())

