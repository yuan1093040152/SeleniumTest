#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/12/31 15:31
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

修改登录人为可登录状态

"""
import MySQLdb,time,os,hashlib,ast

def get_htbh():
    emp_number = os.environ['emp_number']
    print (emp_number)

    # 转换为list的方法：
    import ast
    result = ast.literal_eval(emp_number)
    print(result)
    print(type(result))

    # 创建md5对象并加密
    # md5 = hashlib.md5()
    # b = password.encode(encoding='utf-8')
    # md5.update(b)
    # pass_word = md5.hexdigest()

    for i in result:
        sql = "UPDATE lyj_account_platform.acc_app SET sta = '1',lock_type = '0',et = '0' WHERE emp_no = '%s';"%(i)
        db = MySQLdb.connect(host='172.16.16.31', user='root_t514', passwd='ro1wE1m/0!5_14**#BpT3BkI', port=33096, db='lyj_account_platform',charset='utf8')  # 打开数据库连接\
        cur = db.cursor()  # 使用cursor()方法获取操作游标
        cur.execute(sql)  # 使用execute方法执行SQL语句
        db.commit()  # 提交请求
        print('sql已执行：',sql)
    #values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    cur.close()  # 关闭数据库连接
    return

if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    get_htbh()
