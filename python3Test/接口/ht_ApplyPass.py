#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/1/18 16:06
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import MySQLdb,time,argparse,requests,json

def apply_id(HTBH,url1,url2):

    ht_sql = "SELECT b.APPLY_ID FROM HT_MAIN a RIGHT JOIN APPLY_COMMON b ON a.ID = b.GL_ID WHERE HTBH = '%s'"%HTBH
    print(ht_sql)
    ht = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='jjsht',charset='utf8')  # 打开数据库连接
    ht_cur = ht.cursor()  # 使用cursor()方法获取操作游标
    ht_cur.execute(ht_sql)  # 使用execute方法执行SQL语句
    ht.commit()  # 提交请求
    ht_values = ht_cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    applyId = (ht_values[0][0])
    print(applyId)
    ht_cur.close()  # 关闭数据库连接


    hr_sql = "SELECT * FROM APPROVAL_PEOPLE WHERE APPLY_ID = '%s' ORDER BY ORDER_NUMBER;"%applyId
    print(hr_sql)
    hr = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='workflowplatform', charset='utf8')
    hr_cur = hr.cursor()
    hr_cur.execute(hr_sql)
    hr.commit()
    hr_values = hr_cur.fetchall()
    print(hr_values)
    hr_cur.close()

    for i in hr_values:
        id = i[0]
        APPLY_ID = i[1]
        WORKER_ID = i[2]
        WORKER_NAME = i[3]
        print(id,APPLY_ID,WORKER_ID,WORKER_NAME)

        emp_no_sql = "SELECT emp_no FROM sys_emp WHERE emp_number ='%s';" % WORKER_ID
        print(emp_no_sql)
        hr_no = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='hr',charset='utf8')
        hr_no_cur = hr_no.cursor()
        hr_no_cur.execute(emp_no_sql)
        hr_no.commit()
        hr_no_values = hr_no_cur.fetchall()
        hr_no_cur.close()
        worker_no = hr_no_values[0][0]
        print(worker_no)

        body = 'workerNo='+str(worker_no)+'&wpassword=123456&ckNum=654321&codeVal=0000&needCkNum=true&hddid=&handInfo=&macAddress=6C-0B-84-A4-72-DD'
        headers = {
            'Host': '172.16.22.100',
            'Connection': 'keep-alive',
            'Content-Length': '119',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://172.16.22.100/jjslogin/tologin',
            'Origin':'http://172.16.22.100',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

        requests.packages.urllib3.disable_warnings()  # 移除SSL警告
        response = requests.request("POST", url1, data=body, headers=headers, verify=False)  # ssl验证:verify = False
        # print(response.text)
        cookie = response.cookies.get_dict()
        print(cookie)
        JSESSIONID = cookie['JSESSIONID']
        print(JSESSIONID)
        text = response.text
        load = json.loads(text)
        print('load=',load)
        # token = load['data']['data']['token']
        # print(token)

        body = 'expandJson=%7B%7D&applyId='+str(APPLY_ID)+'&apId='+str(id)+'&annexJson=%5B%5D&type=1&approvalContent=testpass'

        headers = {
            'Host': '172.16.22.100',
            'Connection': 'keep-alive',
            'Content-Length': '97',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://172.16.22.100/workflowplatform/applyInfo/detail?applyId=%s'%APPLY_ID,
            'Origin': 'http://172.16.22.100',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie':'JSESSIONID=%s;login-workerid=%s'%(JSESSIONID,WORKER_ID)
        }

        requests.packages.urllib3.disable_warnings()  # 移除SSL警告
        response = requests.request("POST", url2, data=body, headers=headers, verify=False)  # ssl验证:verify = False
        print(response.text)

    return applyId




if __name__ == '__main__':
    # HTBH = 'ht2021011900001'
    # apply = '1004602'
    url1 = 'http://172.16.22.100/jjslogin/doLoginNew'
    url2 = 'http://172.16.22.100/workflowplatform/applyInfo/approval'
    time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # 获取jenkins传递过来的参数
    parser = argparse.ArgumentParser()
    parser.add_argument("HTBH")
    args = parser.parse_args()
    param = vars(args)
    HTBH = param['HTBH']

    apply_id(HTBH,url1,url2)
