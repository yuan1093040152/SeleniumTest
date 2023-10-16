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


import MySQLdb,time,argparse,os


def get_htbh(HTBH):

    sql = "UPDATE APPLY_COMMON SET SP_STATUS = '2' WHERE GL_ID IN (SELECT bid FROM (SELECT b.GL_ID as bid FROM HT_MAIN a RIGHT JOIN APPLY_COMMON b ON a.ID = b.GL_ID WHERE HTBH = '%s') as tt);"%HTBH
    #sql = "SELECT b.ID,b.HT_ID FROM HT_MAIN a RIGHT JOIN HT_FDD_SIGNER b  ON a.ID = b.HT_ID WHERE a.HTBH = '%s';"%HTBH

    print(sql)

    #获取jenkins执行环境
    huanjing = os.environ['huanjing']
    if huanjing == 'itest':
        db = MySQLdb.connect(host='172.16.22.101', user='idev_user', passwd='IxmTQ_!*OPzNUSKE0V2B3iGI', port=33096, db='jjsht',charset='utf8')  # 打开数据库连接
        print('itest环境已执行')
    elif huanjing == 'onlinetest':
        db = MySQLdb.connect(host='172.16.3.233', user='root', passwd='passwd36', port=34117, db='jjsht',charset='utf8')  # 打开数据库连接
        print('onlinetest环境已执行')

    else:
        print('执行失败，请检查代码！！')


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
    parser.add_argument("HTBH")
    args = parser.parse_args()
    param = vars(args)
    HTBH = param['HTBH']

    get_htbh(HTBH)
