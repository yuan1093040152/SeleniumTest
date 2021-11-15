#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/10 14:23
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import configparser
import os
from UI_jjsAutoTest.UI_jjsAsset.lib.path import CONFIG_PATH


class ReadConfig:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(CONFIG_PATH)


    def get_email(self, mail_key):
        email_value = self.cf.get("EMAIL", mail_key)
        return email_value

    def get_project(self, project_key):
        project_key = self.cf.get("PROJECT", project_key)
        return project_key

    def get_workinfo(self,info_ley):
        info_key = self.cf.get("USERINFO", info_ley)
        return info_key






class MysqlConfig:

    host = '172.16.22.101'
    username = 'root'
    password = 'admintest'
    database = 'bidb_analysis'
    port = 33096


