#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/12/31 15:31
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import MySQLdb,time,argparse,os,hashlib


def get_htbh(emp_number):
    password = os.environ['pass_word']

    # 创建md5对象并加密
    md5 = hashlib.md5()
    b = password.encode(encoding='utf-8')
    md5.update(b)
    pass_word = md5.hexdigest()



    sql = "UPDATE sys_emp_pass SET account_status = '1',login_fail_count = '0',pass_word = '%s' WHERE emp_number = '%s';"%(pass_word,emp_number)

    print(sql)

    db = MySQLdb.connect(host='172.16.3.233', user='root', passwd='passwd36', port=34117, db='hr',charset='utf8')  # 打开数据库连接



    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute(sql)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    #values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    cur.close()  # 关闭数据库连接

    return

if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # 获取jenkins传递过来的参数
    parser = argparse.ArgumentParser()
    parser.add_argument("emp_number")
    args = parser.parse_args()
    param = vars(args)
    emp_number = param['emp_number']

    get_htbh(emp_number)
