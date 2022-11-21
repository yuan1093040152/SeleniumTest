#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/6/23 15:02
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
"""
获取所有股票信息
"""

# 导入tushare
import time,MySQLdb

import tushare as ts
# 初始化pro接口
aa = ts.pro_api('74083a7298dd858297e2379a9e46e23fc9c5d7ae96ab043c649440a4')

# 拉取数据

bb = aa.stock_basic(**{
    "ts_code": "",
    "name": "",
    "exchange": "",
    "market": "",
    "is_hs": "",
    "list_status": "L", #上市状态 L上市 D退市 P暂停上市，默认是L
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "market",
    "list_date",
    "fullname",
    "enname",
    "cnspell",
    "exchange",
    "curr_type",
    "list_status",
    "delist_date",
    "is_hs"
])

# print(bb)

# 行数
rows = bb.shape[0]
# print(rows)

db = MySQLdb.connect(host='localhost', user='root', passwd='admintest', port=3306, db='shares',charset='utf8')  # 打开数据库连接
cur = db.cursor()  # 使用cursor()方法获取操作游标

for i in range(rows):

    c = bb.loc[i]
    print('-------',c['name'])
    sql = "INSERT INTO `shares`.`shareslist` (`ts_code`, `symbol`, `name`, `area`, `industry`, `fullname`, `enname`, `cnspell`, `market`, `exchange`, `curr_type`, `list_status`, `list_date`, `delist_date`,`is_hs`) VALUES ('%s','%s', '%s', '%s', '%s', '%s', NULL,NULL, '%s', '%s', '%s', '%s', NULL, NULL, '%s');"%(c['ts_code'],c['symbol'],c['name'],c['area'],c['industry'],c['fullname'],c['market'],c['exchange'],c['curr_type'],c['list_status'],c['is_hs'])
    print(sql)
    cur.execute(sql)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    # time.sleep(0.1)
cur.close()  # 关闭数据库连接
