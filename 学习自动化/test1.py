#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/11/18 17:45
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import uuid,MySQLdb,time


def get_empNo(emp_number):
    db = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='hr',charset='utf8')  # 打开数据库连接
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute("SELECT emp_number FROM hr.sys_emp WHERE emp_no = '%s';"%emp_number)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    print(values)
    cur.close()  # 关闭数据库连接
    emp_number = values[0][0]
    print(emp_number)
    return emp_number


if __name__ == '__main__':
    get_empNo(emp_number)
