#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/6/23 20:37
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
"""
获取股票每日行情
"""

# 导入tushare
import time,MySQLdb

import tushare as ts
# 初始化pro接口
aa = ts.pro_api('74083a7298dd858297e2379a9e46e23fc9c5d7ae96ab043c649440a4')

trade_date = time.strftime('%Y%m%d', time.localtime(time.time()))
# trade_date = '20220822'
print(trade_date)



# 拉取数据
bb = aa.daily(**{
    "ts_code": "",
    "trade_date": trade_date,
    "start_date": "",
    "end_date": "",
    "offset": "",
    "limit": ""
}, fields=[
    "ts_code",
    "trade_date",
    "open",
    "high",
    "low",
    "close",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
print(bb)

# # 行数
rows = bb.shape[0]
# print(rows)

db = MySQLdb.connect(host='localhost', user='root', passwd='admintest', port=3306, db='shares',charset='utf8')  # 打开数据库连接
cur = db.cursor()  # 使用cursor()方法获取操作游标

for i in range(rows):

    c = bb.loc[i]
    print('-------',c['open'])
    sql = "INSERT INTO `shares`.`sharesquotation` (`ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(c['ts_code'],c['trade_date'],c['open'],c['high'],c['low'],c['close'],c['pre_close'],c['change'],c['pct_chg'],c['vol'],c['amount'])
    print(sql)
    cur.execute(sql)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    # time.sleep(0.1)
cur.close()  # 关闭数据库连接

