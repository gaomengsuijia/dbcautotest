#coding:utf-8
__author__ = "langtuteng"
from driverbase import basedriver
from time import sleep
from appium.webdriver.common.mobileby import By
from selenium.common.exceptions import NoSuchElementException,WebDriverException
class Loginpage(object):
    per_loc = (By.ID,'android:id/button1')
    # login_maintab_loc = (By.ID, "com.ap.dbc.app:id/main_tab_profile_layout")
    login_maintab_loc = (By.ID, "main_tab_profile_layout")
    home_loc = (By.ID, "com.ap.dbc.app:id/main_tab_home_layout")
    login_username_loc = (By.ID,"com.ap.dbc.app:id/et_login_phone")
    login_password_loc = (By.ID,"com.ap.dbc.app:id/et_login_psw")
    login_button_loc = (By.ID,"com.ap.dbc.app:id/bt_login")
    login_head_loc = (By.ID,"com.ap.dbc.app:id/iv_default_heading")
    username = (By.ID,"cn.com.open.mooc:id/account_edit")
    passrword = (By.ID,"cn.com.open.mooc:id/password_edit")
    code = (By.ID,"cn.com.open.mooc:id/et_verification_code")
    log_button = (By.ID,"cn.com.open.mooc:id/login")
    go_log = (By.ID,"cn.com.open.mooc:id/tv_go_login")
    def __init__(self,driver):
        self.dr =  driver

    def __call__(self):
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        pass


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

    #
    # def go_login_page(self):
    #     sleep(2)#等待滑动的页面出现，才开始滑动
    #     for i in range(4):
    #         print('开始滑动%s' % str(i))
    #         self.swipe_left(t=1000)
    #     sleep(3)
    #     # 处理权限弹出窗口
    #     self.get_per()
    #     self.get_per()
    #     # 处理新手引导
    #     sleep(2)
    #     self.dr.mytap([(500, 500)], 500)
    #     sleep(2)
    #     self.dr.findelment(*self.login_maintab_loc).click()
    #     # print(els)

    def find_gologin(self):
        '''
        进入登录页面
        :return:
        '''
        return self.dr.findelment(*self.go_log)


    def find_username_el(self):
        return self.dr.findelment(*self.username)

    def find_password_el(self):
        return self.dr.findelment(*self.passrword)


    def find_code_el(self):
        return self.dr.findelment(*self.code)


    def find_login_el(self):
        return self.dr.findelment(*self.log_button)




if __name__ == "__main__":
    driver = basedriver.Basedriver()
    sleep(3)
    loginpage = Loginpage(driver)
    sleep(2)
    loginpage.go_login()



