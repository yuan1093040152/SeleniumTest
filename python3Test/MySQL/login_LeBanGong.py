#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/11/18 17:45
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import uuid,MySQLdb,time,argparse


def get_empNo(emp_number):
    db = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='hr',charset='utf8')  # 打开数据库连接
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute("SELECT emp_number FROM hr.sys_emp WHERE emp_no = '%s';"%emp_number)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    if len(values)==0:
        print('工号输入有误，查询不到人员信息！')
    else:
        print(values)
        cur.close()  # 关闭数据库连接
        emp_number = values[0][0]
        print(emp_number)
        return emp_number


def get_empNumber(emp_number):
    db = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='hr',charset='utf8')  # 打开数据库连接
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute("SELECT emp_number FROM hr.sys_emp WHERE emp_number = '%s';"%emp_number)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    if len(values)==0:
        print('编号输入有误，查询不到人员信息！')
    else:
        print(values)
        cur.close()  # 关闭数据库连接
        emp_number = values[0][0]
        print(emp_number)
        return emp_number


def create_user(emp_number4):
    db = MySQLdb.connect(host='172.16.22.101', user='root', passwd='admintest', port=33096, db='hr',charset='utf8')  # 打开数据库连接
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute("UPDATE hr.sys_emp SET login_status = '3' , emp_status = '3' , account_status = '1' , status = '3' WHERE emp_number = '%s';" % emp_number4)  # 使用execute方法执行SQL语句
    cur.execute("INSERT INTO `hr`.`sys_loginUser` (`emp_number`, `password`, `status`, `BI_DATE`) VALUES ('%s', 'e10adc3949ba59abbe56e057f20f883e', '3', '2020-03-21 10:33:41');" % emp_number4)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    cur.close()  # 关闭数据库连接





def main(emp_number):
    try:

        if len(emp_number) == 6:
            empNumber4=get_empNo(emp_number)
            if empNumber4==None:
                print('工号输入有误，查询不到人员信息！')

            else:
                create_user(empNumber4)
                time.sleep(1)
                print('通过员工工号创建成功，可登陆乐办公啦！')



        elif len(emp_number) == 8:
            empNumber4 = get_empNumber(emp_number)
            if empNumber4 == None:
                print('编号输入有误，查询不到人员信息！')

            else:
                create_user(emp_number)
                time.sleep(1)
                print('通过员工编号创建成功，可登陆乐办公啦！')


        else:
            print('请输入正确的员工工号（六位）和正确的员工编号（八位）')
    except :
        print('输入有误,请检查输入内容')



if __name__ == '__main__':
    #获取jenkins传递过来的参数
    parser = argparse.ArgumentParser()
    parser.add_argument("emp_number")
    args = parser.parse_args()
    param = vars(args)
    emp_number = param['emp_number']
    print('emp_number',emp_number)

    # emp_number = '90300005'

    main(emp_number)


