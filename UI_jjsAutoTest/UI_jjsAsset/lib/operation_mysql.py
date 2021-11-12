#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/10 14:21
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""



import pymysql
from UI_jjsAutoTest.UI_jjsAsset.config.readconfig import MysqlConfig

class MysqlServer(object):

    def __init__(self):
        self.host = MysqlConfig.host
        self.username = MysqlConfig.username
        self.password = MysqlConfig.password
        self.database = MysqlConfig.database
        self.port = MysqlConfig.port
        self.db = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.username,
                                     password=self.password,
                                     db=self.database,
                                     charset="utf8mb4",
                                     cursorclass=pymysql.cursors.DictCursor
                                     )


    def delete(self,sql):

        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as error:
            print('delete error:',error)
            self.db.rollback()
        finally:
            self.cursor.close()


    def closedb(self):

        self.db.close()


if __name__ == '__main__':
    Mysql = MysqlServer()
    #data = Mysql.delete("DELETE FROM bello_user WHERE emp_name LIKE '梁洁仪Z%';")
    Mysql.closedb()
