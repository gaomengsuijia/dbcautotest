#coding:utf-8

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def mycaps(platformName,platformVersion,deviceName,autoLaunch,appPackage,appActivity='com.ap.dbc.app.SplashActivity'):
    print(BASE_DIR)
    desired_caps = {}
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['autoLaunch'] = autoLaunch
    #desired_caps['app'] = conf.PATH
    desired_caps['appPackage'] = appPackage
    #desired_caps['appActivity'] = '.ui.activity.LoginActivity'
    desired_caps['appActivity'] = appActivity
    return desired_caps


