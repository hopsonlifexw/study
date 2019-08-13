#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/28
# @Author  : vivid-XIEMENG
# @FileName: test_mp_login.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

import unittest
from  BeautifulReport import BeautifulReport
from DestroyerRobot.automation.com.cn.util.ConfigUtil import Config
from DestroyerRobot.automation.com.cn.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.com.cn.util.DateTimeUtil import TestDateTime
class testFileReport:
    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("markerting_points_configs")
        return confFile

    def childConfigReport(self):
        # "获取子配置文件中信息",report
        confFile = self.rootChildConfigPath()
        config1= Config("ReportFile",confFile)
        mpreport= config1.get_path_config("mpReport")
        return mpreport

    def childConfigTestFile(self):
        # "获取子配置文件中信息",testFile
        confFile = self.rootChildConfigPath()
        config1 = Config("TestFile", confFile)
        testFile = config1.get_path_config("mprTestFile")
        return testFile

if __name__ == '__main__':
    test_report = testFileReport()
    test_dir =SystemOs().sys_path(test_report.childConfigTestFile())
    report_dir = SystemOs().sys_path(test_report.childConfigReport())
    print(report_dir)
    discover = unittest.defaultTestLoader.discover(test_dir,'test_*.py',None)
    filename = '测试报告'+str(TestDateTime().report_file())
    BeautifulReport(discover).report(description='测试',filename=filename,report_dir=report_dir)
