#coding:utf-8
__author__ = "langtuteng"
import configparser



def readconfig(file_path='../conf/capability.conf'):
    '''
    读取配置文件
    :param file_path:
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(file_path)
    platformName = conf.get('desired_caps','platformName')
    platformVersion = conf.get('desired_caps','platformVersion')
    deviceName = conf.get('desired_caps','deviceName')
    autoLaunch = conf.get('desired_caps','autoLaunch')
    app = conf.get('desired_caps','app')
    appPackage = conf.get('desired_caps','appPackage')
    appActivity = conf.get('desired_caps','appActivity')
    return {'platformName':platformName,'platformVersion':platformVersion,
            'deviceName':deviceName,'autoLaunch':autoLaunch,
            'app':app,'appPackage':appPackage,'appActivity':appActivity }


def writeconfig(file_path):
    conf = configparser.ConfigParser()
    conf.read(file_path)
    # 写配置文件

    # 更新指定section, option的值
    conf.set("section2", "port", "8081")

    # 写入指定section, 增加新option的值
    conf.set("section2", "IEPort", "80")

    # 添加新的 section
    conf.add_section("new_section")
    conf.set("new_section", "new_option", "http://www.cnblogs.com/tankxiao")

    # 写回配置文件
    conf.write(open("c:\\test.conf", "w"))
    return True



if __name__ == "__main__":
    print(readconfig('../conf/capability.conf'))