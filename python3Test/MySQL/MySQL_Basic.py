#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/7/30 18:21
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import pymysql

class Connect_database(object):


    def __init__(self):

        hosts = '172.16.22.101'
        port = 33096  #不能加引号，不能以字符串传值
        user = 'root'
        password = 'admintest'
        db = 'jjsht'

        self.db = pymysql.connect(host=hosts, port=port, user=user, password=password, db=db,charset='utf8mb4')


    def insertDB(self, sql):
        """插入数据"""
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('insert data error:', err)
            self.db.rollback()  # 发生错误时回滚
        finally:
            self.cursor.close()


    def deleteDB(self, sql):
        """删除数据"""
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('delete data error:', err)
            self.db.rollback()
        finally:
            self.cursor.close()

    def updateDB(self, sql):
        """修改数据"""
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('update data error:', err)
            self.db.rollback()
        finally:
            self.cursor.close()

    def selectDB(self, sql):
        """查询数据"""
        self.cursor = self.db.cursor()  # 以元组格式返回查询结果
        # self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor) # 查以字典格式返回查询结果
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except Exception as err:
            data = tuple()
            print('select data error:', err)
        finally:
            self.cursor.close()
        return data

    def closeDB(self):
        """关闭数据库连接"""
        self.db.close()



if __name__ == '__main__':

    a = Connect_database().selectDB("SELECT * FROM HT_FDD_SIGNER GROUP BY INSERTTIME DESC LIMIT 10;")
    print(a)
