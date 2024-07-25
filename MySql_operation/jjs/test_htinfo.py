#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2024/7/25 18:13
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


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
import pandas as pd
import MySQLdb,os,json



class ht_info:

    #获取jenkins传参
    def __init__(self):
        # self.lx = os.environ['lx']
        # self.cjdh = os.environ['cjdh']
        # self.env = os.environ['env']
        # self.yz = os.environ['yz']
        # self.kh = os.environ['kh']
        self.lx = '买卖电子合同'
        self.cjdh = 'M3012407-0117'
        self.env = 'UAT'
        self.yz = '袁猛'
        self.kh = '李益祯'


    #转义jenkins传参数据
    def htlx(self):
        if self.lx =='租赁电子合同':
            return 1
        elif self.lx =='买卖电子合同':
            return 2
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


    def auth_info(self):
        sql_yz = "SELECT a.`name`,a.id_number,a.tel FROM test_auth a WHERE emp_type = '1' AND cust_type = '1' AND `name` = '%s';"%self.yz
        sql_kh = "SELECT a.`name`,a.id_number,a.tel FROM test_auth a WHERE emp_type = '1' AND cust_type = '2' AND `name` = '%s';"%self.kh
        db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117,
                             db='fastrunner',
                             charset='utf8')  # 打开数据库连接
        cur = db.cursor()  # 获取操作游标
        aa = []
        for sql in (sql_yz,sql_kh):
            cur.execute(sql)  # 执行SQL语句
            db.commit()  # 提交请求
            values = cur.fetchall()  # 获取一条数据
            extend_json = values[0]
            aa.append(extend_json)
        print(aa)
        return aa






    def get_json(self):
        wymc = self.get_wymc()
        info = self.auth_info()
        sql = "SELECT a.extend_json FROM test_htinfo a WHERE WYMC = '%s';"%wymc
        db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117,
                             db='fastrunner',
                             charset='utf8')  # 打开数据库连接
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql)  # 执行SQL语句
        db.commit()  # 提交请求
        values = cur.fetchall()  # 获取一条数据
        if len(values) == 0:
            print('该成交单号未查询到成交信息，请检查是否填写正确！')
        else:
            cur.close()  # 关闭数据库连接
            extend_json = values[0][0]

            a = json.loads(extend_json)
            yzinfo = a['yzInfo']['list'][0]
            yzinfo['ppName'] = info[0][0]
            yzinfo['ppZj'] = info[0][1]
            yzinfo['ppDhhm'] = info[0][2]

            khinfo = a['khInfo']['list'][0]
            khinfo['ppName']=info[1][0]
            khinfo['ppZj'] = info[1][1]
            khinfo['ppDhhm'] = info[1][2]

            print(a)
            return a

            #extend_json1 = eval(extend_json)
            #print(type(a))
            #return extend_json




    # def redeExcel(self):
    #     # 读取Excel文件
    #     df = pd.read_excel('E:\\test\\ht\\htinfo.xlsx', sheet_name='Sheet1')
    #
    #     # 读取指定位置的单元格值
    #     if self.htlx() ==1:
    #         value = df.iloc[0, 1]
    #         return value
    #     elif self.htlx() ==2:
    #         value = df.iloc[1, 1]
    #         return value
    #     elif self.htlx() ==3:
    #         value = df.iloc[2, 1]
    #         return value
    #     else:
    #         print('传值错误，无法生成合同')


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
            # return htid


    #通过成交ID修改json数据
    def fill_ht(self):

        global db
        sql = "UPDATE HT_MAIN SET EXTEND_JSON = '%s' WHERE ID = '%s';" % (str(self.get_json()),self.get_htid())
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