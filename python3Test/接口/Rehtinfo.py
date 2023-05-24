#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/5/24 10:45
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import requests,MySQLdb,time,argparse,os,hashlib

company = os.environ['company']
# company = '佛山乐有家'
cj_id = os.environ['cj_id']
# cj_id = '82149706e01146eebee7cc719097e801'

def sys_company(company):

    sql = "SELECT old_id FROM sys_company WHERE cm_short_name = '%s' AND cm_state = '1';"%company
    print('sql===',sql)
    db = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='hr',charset='utf8')  # 打开数据库连接

    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute(sql)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    values = (cur.fetchall())[0][0]  # 使用 fetchone() 方法获取一条数据
    print(values)
    cur.close()  # 关闭数据库连接

    return values


def t_main_base(company,cj_id):
    company_id = sys_company(company)
    sql = "UPDATE t_main_base SET company_id = '%s',company_name = '%s' WHERE id = '%s';"%(company_id,company,cj_id)
    print('sql===', sql)
    db = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='lyj_trade',charset='utf8')  # 打开数据库连接
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute(sql)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    # values = (cur.fetchall())[0][0]  # 使用 fetchone() 方法获取一条数据
    # print(values)
    cur.close()  # 关闭数据库连接

    return



def RefreshHtinfo(cj_id):

    url = "https://itest.leyoujia.com/trade-means/inner/zl-main/createZl/%s"%cj_id

    headers = {
        'cache-control': "no-cache",
        'postman-token': "e77e0bc4-00c0-b562-e209-bf5b34cbee0d"
        }

    response = requests.request("POST", url, headers=headers)

    print(response.text)



if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    t_main_base(company, cj_id)
    RefreshHtinfo(cj_id)