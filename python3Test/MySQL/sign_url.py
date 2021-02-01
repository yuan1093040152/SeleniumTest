#coding=utf-8
import MySQLdb,time,argparse


def get_htbh(HTBH):

    sql = "SELECT b.ID,b.HT_ID FROM HT_MAIN a RIGHT JOIN HT_FDD_SIGNER b  ON a.ID = b.HT_ID WHERE b.SIGN_STATUS = '7' AND a.HTBH = '%s';"%HTBH
    #sql = "SELECT b.ID,b.HT_ID FROM HT_MAIN a RIGHT JOIN HT_FDD_SIGNER b  ON a.ID = b.HT_ID WHERE a.HTBH = '%s';"%HTBH

    print(sql)

    db = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='jjsht',charset='utf8')  # 打开数据库连接
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute(sql)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    cur.close()  # 关闭数据库连接
    # return values

    print(values)
    cc = []
    try:

        HT_ID = values[0][1]
        print(HT_ID)
        for i in values:
            QS_ID = i[0]
            print(QS_ID)

            a = 'http://itest.leyoujia.com/jjsht/fddThird/gotoSignPage/%s/%s'%(HT_ID,QS_ID)

            print(a)
            cc.append(a)
    except:
        print('未找到需要签署的信息，请确认签署人是否已实名认证')
        pass
    print(cc)
    return cc

if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # 获取jenkins传递过来的参数
    parser = argparse.ArgumentParser()
    parser.add_argument("HTBH")
    args = parser.parse_args()
    param = vars(args)
    HTBH = param['HTBH']

    get_htbh(HTBH)


