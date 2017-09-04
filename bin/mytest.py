from appium import webdriver
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import conf
import time
from testcase import login_test

# desired_caps = mycaps('Android','4.4.2','ecd832cc','true','com.ap.dbc.app','com.ap.dbc.app.DbcMainActivity')
# desired_caps = mycaps('Android','4.4.2','6248724d','true','com.ap.dbc.app','.DbcMainActivity')
mydriver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(8)
# mydriver.find_element_by_id('com.ap.dbc.app:id/main_tab_profile_layout').click()
mydriver.find_element_by_id('com.ap.dbc.app:id/main_tab_profile_layout').click()
# login
time.sleep(3)
mydriver.find_element_by_id('com.ap.dbc.app:id/iv_default_heading').click()
time.sleep(3)
mydriver.find_element_by_id('com.ap.dbc.app:id/et_login_phone').send_keys('18565660212')
time.sleep(2)
mydriver.find_element_by_id('com.ap.dbc.app:id/et_login_psw').send_keys('123456')
time.sleep(2)
mydriver.find_element_by_id('com.ap.dbc.app:id/bt_login').click()