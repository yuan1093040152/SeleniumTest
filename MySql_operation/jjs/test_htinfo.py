#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/9/18 11:34
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import MySQLdb,os,json

class ht_info:

    #获取jenkins传参
    def __init__(self):
        self.lx = os.environ['lx']
        self.cjdh = os.environ['cjdh']
        self.env = os.environ['env']
        # self.lx = '租赁合同'
        # self.cjdh = 'Z3012601-0128'
        # self.env = 'itest'

    #转义jenkins传参数据
    def htlx(self):
        if self.lx =='租赁合同':
            return 12
        elif self.lx =='买卖合同':
            return 4
        else:
            return 1

    def get_wymc(self):
        global db
        sql = "SELECT a.WYMC FROM CJ_MAIN a WHERE GZDH = '%s';"%self.cjdh
        print("获取物业名称SQL为：", sql)
        huanjing = self.env
        if huanjing == 'itest':
            db = MySQLdb.connect(host='172.16.22.101', user='idev_user', passwd='IxmTQ_!*OPzNUSKE0V2B3iGI', port=33096,
                                 db='jjscj',
                                 charset='utf8')  # 打开数据库连接
            print('itest环境已执行')
        elif huanjing == 'UAT':
            db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117,
                                 db='jjscj',
                                 charset='utf8')  # 打开数据库连接
            print('onlinetest环境已执行')
        elif huanjing == '3.100':
            db = MySQLdb.connect(host='172.16.3.230', user='root_u3230', passwd='Nb37GxP&3_230**#ETwgps4Nq', port=33096,
                                 db='jjscj',
                                 charset='utf8')  # 打开数据库连接
            print('3.100环境已执行')
        else:
            print('执行失败，请检查代码！！')

        cur = db.cursor()  # 获取操作游标
        cur.execute(sql)  # 执行SQL语句
        db.commit()  # 提交请求
        values = cur.fetchall()  # 获取一条数据
        if len(values) == 0:
            print('该成交单号未查询到成交信息，请检查是否填写正确！')
        else:
            cur.close()  # 关闭数据库连接
            htid = values[0][0]
            print(htid)
            return htid

    def get_json(self):
        wymc = self.get_wymc()
        sql = "SELECT a.EXTEND_JSON FROM HT_MAIN a WHERE WYMC = '%s' AND YWLX = '%s' AND XYLX IN(11,13) AND `STATUS` IN(8,7)  AND EXTEND_JSON NOT LIKE '%%appVersion%%'  AND GZDH IS NOT NULL ORDER BY INSERT_TIME DESC LIMIT 1 ;" % (wymc,self.htlx())
        print(sql)
        db1 = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117,
                             db='jjsht',  #fastrunner
                             charset='utf8')  # 打开数据库连接

        db = MySQLdb.connect(host='172.16.22.101', user='idev_user', passwd='IxmTQ_!*OPzNUSKE0V2B3iGI', port=33096,
                             db='jjsht',
                             charset='utf8')  # 打开数据库连接

        cur = db.cursor()  # 获取操作游标
        cur.execute(sql)  # 执行SQL语句
        db.commit()  # 提交请求
        values = cur.fetchall()  # 获取一条数据
        if len(values) == 0:
            print("itest没找到数据，现在去UAT找数据")
            cur = db1.cursor()  # 获取操作游标
            cur.execute(sql)  # 执行SQL语句
            db.commit()  # 提交请求
            values = cur.fetchall()  # 获取一条数据
            cur.close()  # 关闭数据库连接
            extend_json = values[0][0]
            a = json.loads(extend_json)
        else:
            print("itest 找到了数据，优先同步itest的数据")
            cur.close()  # 关闭数据库连接
            extend_json = values[0][0]
            a = json.loads(extend_json)


    #通过成交单号获取合同ID
    def get_htid(self):
        global db
        sql = "SELECT a.HT_ID FROM CJ_MAIN a WHERE GZDH = '%s';"%self.cjdh
        print("获取合同IDsql为：",sql)
        huanjing = self.env
        if huanjing == 'itest':
            db = MySQLdb.connect(host='172.16.22.101', user='idev_user', passwd='IxmTQ_!*OPzNUSKE0V2B3iGI', port=33096, db='jjscj',
                                 charset='utf8')  # 打开数据库连接
            print('itest环境已执行')
        elif huanjing == 'UAT':
            db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117, db='jjscj',
                                 charset='utf8')  # 打开数据库连接
            print('onlinetest环境已执行')
        elif huanjing == '3.100':
            db = MySQLdb.connect(host='172.16.3.230', user='root_u3230', passwd='Nb37GxP&3_230**#ETwgps4Nq', port=33096, db='jjscj',
                                 charset='utf8')  # 打开数据库连接
            print('3.100环境已执行')
        else:
            print('执行失败，请检查代码！！')

        cur = db.cursor()  # 获取操作游标
        cur.execute(sql)  # 执行SQL语句
        db.commit()  # 提交请求
        values = cur.fetchall()  # 获取一条数据
        if len(values) == 0:
            print('该成交单号未查询到成交信息，请检查是否填写正确！')
        else:
            cur.close()  # 关闭数据库连接
            htid = values[0][0]
            print(type(htid))
            return htid


    #通过成交ID修改json数据
    def fill_ht(self):
        global db
        # IFnew = self.IFnew()
        wymc = self.get_wymc()
        htid = self.get_htid()

        # if IFnew == 2:
        print('新版合同不更换签约人')
        sql = "UPDATE jjsht.HT_MAIN SET EXTEND_JSON = (SELECT EXTEND_JSON FROM ( SELECT a.EXTEND_JSON FROM HT_MAIN a WHERE WYMC = '%s' AND YWLX = '%s' AND XYLX IN (11, 13) AND `STATUS` IN (8, 7) AND EXTEND_JSON NOT LIKE '%%appVersion%%' AND GZDH IS NOT NULL ORDER BY INSERT_TIME DESC LIMIT 1 ) AS subquery ) WHERE ID = '%s';"%(wymc,self.htlx(),htid)
        print(sql)

        # 获取jenkins执行环境
        huanjing = self.env
        if huanjing == 'itest':
            db = MySQLdb.connect(host='172.16.22.101', user='idev_user', passwd='IxmTQ_!*OPzNUSKE0V2B3iGI', port=33096, db='jjsht',
                                 charset='utf8')  # 打开数据库连接
            print('itest环境已执行')
        elif huanjing == 'UAT':
            db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117, db='jjsht',
                                 charset='utf8')  # 打开数据库连接
            print('onlinetest环境已执行')
        elif huanjing == '3.100':
            db = MySQLdb.connect(host='172.16.3.230', user='root_u3230', passwd='Nb37GxP&3_230**#ETwgps4Nq', port=33096, db='jjsht',
                                 charset='utf8')  # 打开数据库连接
            print('3.100环境已执行')
        else:
            print('执行失败，请检查代码！！')

        cur = db.cursor()  # 获取操作游标
        cur.execute(sql)  # 执行SQL语句
        db.commit()  # 提交请求
        cur.close()  # 关闭数据库连接
        return

if __name__ == '__main__':
    ht_info().fill_ht()