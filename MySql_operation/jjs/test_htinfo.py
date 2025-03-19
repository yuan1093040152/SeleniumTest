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
        self.lx = os.environ['lx']
        self.cjdh = os.environ['cjdh']
        self.env = os.environ['env']
        self.yz = os.environ['yz']
        self.kh = os.environ['kh']
        self.ifnew = os.environ['ifnew']
        # self.lx = '买卖电子合同'
        # self.cjdh = 'M1112407-0121'
        # self.env = 'UAT'
        # self.yz = '袁猛'
        # self.kh = '李益祯'
        # self.ifnew = '旧合同（移动端）'


    #转义jenkins传参数据
    def htlx(self):
        if self.lx =='租赁电子合同':
            return 12
        elif self.lx =='买卖电子合同':
            return 4
        else:
            return 1

    def IFnew(self):
        if self.ifnew == '旧合同（移动端）':
            return 1
        elif self.ifnew == '新合同（前端）':
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
        IFnew = self.IFnew()

        #sql = "SELECT a.extend_json FROM test_htinfo a WHERE YWLX = '%s' AND WYMC = '%s';"%(self.htlx(),wymc)
        if IFnew==1:
            sql = "SELECT a.EXTEND_JSON FROM HT_MAIN a WHERE WYMC = '%s' AND YWLX = '%s' AND XYLX IN(11,13) AND `STATUS` IN(8,7)  AND EXTEND_JSON NOT LIKE '%%appVersion%%'  AND GZDH IS NOT NULL ORDER BY INSERT_TIME DESC LIMIT 1 ;" % (wymc,self.htlx())
        elif IFnew ==2:
            sql = "SELECT a.EXTEND_JSON FROM HT_MAIN a WHERE WYMC = '%s' AND YWLX = '%s' AND XYLX IN(11,13) AND `STATUS` IN(8,7)  AND EXTEND_JSON LIKE '%%appVersion%%'  AND GZDH IS NOT NULL ORDER BY INSERT_TIME DESC LIMIT 1 ;" % (wymc,self.htlx())
        else:
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
            print('extend_json==========', extend_json)

            a = json.loads(extend_json)
            print('------------', a)
            #判断新合同就不更换签约人
            IFnew = self.IFnew()
            if IFnew =='2':
                print('新版合同不更换签约人')
                cur.close()  # 关闭数据库连接
            else:
                #租单和售单分开处理
                if self.htlx() ==4:
                    yzinfo = a['yzInfo']['list'][0]
                    yzinfo['ppName'] = info[0][0]
                    yzinfo['ppZj'] = info[0][1]
                    yzinfo['ppDhhm'] = info[0][2]

                    khinfo = a['khInfo']['list'][0]
                    khinfo['ppName'] = info[1][0]
                    khinfo['ppZj'] = info[1][1]
                    khinfo['ppDhhm'] = info[1][2]
                    b = json.dumps(a, ensure_ascii=False)
                    b = b.replace('\\"', '\\\\"')
                    print('==========', b)
                    return b

                elif self.htlx() ==12:
                    yzinfo = a['yzInfo'][0]
                    yzinfo['name'] = info[0][0]
                    yzinfo['idCard'] = info[0][1]
                    yzinfo['tel'] = info[0][2]

                    khinfo = a['khInfo'][0]
                    khinfo['name'] = info[1][0]
                    khinfo['idCard'] = info[1][1]
                    khinfo['tel'] = info[1][2]
                    b = json.dumps(a, ensure_ascii=False)
                    b = b.replace('\\"', '\\\\"')
                    print('==========', b)
                    return b
                else:
                    print('该成交单号未查询到成交信息，请检查是否填写正确！')
                    cur.close()  # 关闭数据库连接



        else:
            print("itest 找到了数据，优先同步itest的数据")
            cur.close()  # 关闭数据库连接
            extend_json = values[0][0]
            print('extend_json==========',extend_json)

            a = json.loads(extend_json)
            print('------------',a)

            # 租单和售单分开处理
            if self.htlx() == 4:
                yzinfo = a['yzInfo']['list'][0]
                yzinfo['ppName'] = info[0][0]
                yzinfo['ppZj'] = info[0][1]
                yzinfo['ppDhhm'] = info[0][2]

                khinfo = a['khInfo']['list'][0]
                khinfo['ppName'] = info[1][0]
                khinfo['ppZj'] = info[1][1]
                khinfo['ppDhhm'] = info[1][2]
                b = json.dumps(a, ensure_ascii=False)
                b = b.replace('\\"', '\\\\"')
                print('==========', b)
                return b

            elif self.htlx() == 12:
                yzinfo = a['yzInfo'][0]
                yzinfo['name'] = info[0][0]
                yzinfo['idCard'] = info[0][1]
                yzinfo['tel'] = info[0][2]

                khinfo = a['khInfo'][0]
                khinfo['name'] = info[1][0]
                khinfo['idCard'] = info[1][1]
                khinfo['tel'] = info[1][2]
                b = json.dumps(a, ensure_ascii=False)
                b = b.replace('\\"', '\\\\"')
                print('==========', b)
                return b
            else:
                print('该成交单号未查询到成交信息，请检查是否填写正确！')
                cur.close()  # 关闭数据库连接





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
            return htid


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