#coding:utf-8
__author__ = "langtuteng"
from driverbase import basedriver
from time import sleep
from appium.webdriver.common.mobileby import By
from selenium.common.exceptions import NoSuchElementException,WebDriverException
class Loginpage(object):
    per_loc = (By.ID,'android:id/button1')
    login_maintab_loc = (By.ID, "com.ap.dbc.app:id/main_tab_profile_layout")
    login_username_loc = (By.ID,"com.ap.dbc.app:id/et_login_phone")
    login_password_loc = (By.ID,"com.ap.dbc.app:id/et_login_psw")
    login_button_loc = (By.ID,"com.ap.dbc.app:id/bt_login")
    login_head_loc = (By.ID,"com.ap.dbc.app:id/iv_default_heading")
    def __init__(self,driver):
        self.dr =  driver

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
        l = self.dr.get_wind_size()
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.dr.myswipe(x1,y1,x2,y1,t)


    def swipe_right(self,t=1000):
        '''
        向右滑动
        @t 滑动时间
        :return:
        '''
        l = self.dr.get_wind_size()
        x1 = int(l[0]*0.25)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.75)
        self.dr.myswipe(x1,y1,x2,y1,t)

    def swipe_top(self,t=1000):
        '''
        向上滑动
        :param t:
        :return:
        '''
        l = self.dr.get_wind_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[1] * 0.9)
        self.dr.myswipe(x1, y1, x1, y2, t)

    def swipe_bottom(self,t=1000):
        '''
        向下滑动
        :param t:
        :return:
        '''
        l = l = self.dr.get_wind_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.1)
        self.dr.myswipe(x1, y1, x1, y2, t)

    def get_per(self):
        try:
            per = self.dr.findelment(*self.per_loc)
            per.click()
        except NoSuchElementException as e:
            print("找不到元素")


    # def tap_screen(self,position,duration):
    #     self.driver.mytap(position,duration)


    def go_login_page(self):
        sleep(2)#等待滑动的页面出现，才开始滑动
        for i in range(5):
            print('开始滑动%s' % str(i))
            self.swipe_left(t=1000)
        sleep(4)
        # 处理权限弹出窗口
        self.get_per()
        self.get_per()

        # 处理新手引导
        self.dr.mytap([(500, 500)], 500)
        sleep(2)
        #点击进入登录页面
        self.dr.mytap([(500, 500)], 500)
        sleep(3)
        self.find_login_main().click()
        sleep(2)


    def find_login_main(self):
        self.dr.findelment(*self.login_maintab_loc)

    def find_username_el(self):
        self.dr.findelment(*self.login_username_loc)

    def find_password_el(self):
        self.dr.findelment(*self.login_password_loc)


    def find_login_el(self):
        self.dr.findelment(*self.login_button_loc)




if __name__ == "__main__":
    driver = basedriver.Basedriver()
    loginpage = Loginpage(driver)
    sleep(2)
    loginpage.go_login_page()




