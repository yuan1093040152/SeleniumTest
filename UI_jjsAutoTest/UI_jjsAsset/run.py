#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/12 14:37
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import argparse
import datetime
import sys
import unittest,time
import uuid

import requests
from BeautifulReport import BeautifulReport
import os
import time
from UI_jjsAutoTest.UI_jjsAsset.config.readconfig import ReadConfig
from UI_jjsAutoTest.UI_jjsAsset.lib.path import mainpath,test_case_path,report_path,CASEDIR
from UI_jjsAutoTest.UI_jjsAsset.lib.HTMLTestRunner import HTMLTestRunner
# from lib.sendemail import SendEmail
# from lib.download_driver import osSystem
from UI_jjsAutoTest.UI_jjsAsset.lib.tool import delreport
from UI_jjsAutoTest.UI_jjsAsset.lib.sendemall import SendEmail
from UI_jjsAutoTest.UI_jjsAsset.lib.operation_mysql import MysqlServer



local_readConfig = ReadConfig()
# SendEmail = SendEmail()


# class Main:
#     def __init__(self):
#         global title
#         title = local_readConfig.get_project('title')
#     def run(self):
#         delreport()
#         suite = unittest.TestSuite()
#
#         cases = unittest.defaultTestLoader.discover(test_case_path)
#         for case in cases:
#             suite.addTest(case)
#         now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
#         filename = report_path + os.path.sep + now +'report.html'
#         f = open(filename ,'wb')
#         runner = HTMLTestRunner(f,verbosity=2,title=u'%s'%title, description=u'用例执行情况：')
#         runner.run(suite)
#         f.flush()
#         f.close()
#         print('测试报告已生成，路径：%s'%filename)


        # 方法2
        # tests = unittest.defaultTestLoader.discover(test_case_path,pattern='test_gzgl*.py',top_level_dir=None) #找指定路径下以.py结尾的文件
        # runner = BeautifulReport(tests)#运行找到的所有用例
        # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        # filename = '%s-report.html'%now #报告文件名
        # runner.report('自动化测试报告',filename=filename,report_dir=report_path)#产生报告

        #发送邮件
        # SendEmail.Email(file=filename)

# if __name__ == '__main__':
#     Main().run()




class Main:
    def __init__(self):
        global title
        # self.send_mail = SendEmail()
        title = local_readConfig.get_project('title')
        self.m = MysqlServer()

    def save_report(self, pathname):
        """
        # 上传日志文件到服务器
        :param pathname: 完整的日志文件路径
        :param field_name: 在服务器端，重命名文件名
        :return:
        """
        try:
            # 当前日志完整路径
            field_name = pathname.split(os.path.sep)[-1]
            # 读取文件
            # with open(pathname, 'rb') as f:
            #     # files = f.read()
            files = {'file': open(pathname, 'rb')}
            upload_data = {"file_name": field_name}
            upload_res = requests.post('http://14.116.157.229:29998/netsavelog', upload_data, files=files, timeout=30)
            if upload_res.status_code == 200:
                return f"http://14.116.157.229:29998/netreadlog/{field_name}"
            return " "
        except:
            return " "

    def run(self, argparam:dict):
        # osSystem()
        delreport()
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        case_path = argparam.get("case_dir")
        build_list = argparam.get("build")
        # build_list = build_data.split(",")
        if len(build_list) != 3:
            raise RuntimeError("构建信息填写错误")
        env = argparam.get('env')
        headless = argparam.get('headless')
        if headless:
            local_readConfig.write_conf('PROJECT', 'headless', headless)

        if case_path is None:
            case_path = CASEDIR

        case_path_list = case_path.split(",")

        for item in case_path_list:
            case_path = os.path.join(mainpath, item)
            if not os.path.exists(case_path):
                raise RuntimeError("用例地址不存在")

            case_dir = []
            if os.path.isdir(case_path):
                case_dir = unittest.defaultTestLoader.discover(case_path)
            if os.path.isfile(case_path):
                file_name = case_path.split('\\')[-1]
                case_path = case_path.replace(file_name, "")
                suite.addTest(loader.discover(case_path, pattern=file_name))
            for case in case_dir:
                suite.addTest(case)


        start_time = time.localtime(time.time())
        now = time.strftime("%Y-%m-%d_%H-%M-%S", start_time)
        filename = mainpath + os.path.sep + 'report' + os.path.sep + now +'report.html'
        f = open(filename, 'wb')
        # runner = HTMLTestRunner(f,verbosity=2,title=u'%s'%title, description=u'用例执行情况：')
        runner = HTMLTestRunner(f,verbosity=2,title=u'%s测试报告'%title, description=u'用例执行情况：')
        res = runner.run(suite)
        test_case = runner.all_test_case
        f.flush()
        f.close()
        end_time = time.localtime(time.time())
        report_url = self.save_report(filename)
        if int(argparam.get("debug")) == 0:
            result_id = str(uuid.uuid1())
            insert_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = f"""
            INSERT INTO tapd.auto_ui_result (
            project_name,
            result_id,
            total_case_num,
            success_num,
            fail_num,
            report_url,
            insert_time,
            env,
            error_num,
            build_name,
            build_code,
            start_time,
            end_time,
            iteration_name
        )
        VALUES
            (
                '{title}',
                '{result_id}',
                {res.success_count+res.failure_count+res.error_count},
                {res.success_count},
                {res.failure_count},
                '{report_url}',
                '{insert_time}',
                '{env}',
                {res.error_count},
                '{build_list[0]}',
                '{build_list[1]}',
                '{time.strftime("%Y-%m-%d %H:%M:%S", start_time)}',
                '{time.strftime("%Y-%m-%d %H:%M:%S", end_time)}',
                '{build_list[2]}'
            );
            """
            self.m.insertDB(sql)

            self.insert_case_res(test_case, result_id, build_list[1])

        # self.send_mail.send_email()

        if res.failure_count == 0 and res.error_count == 0:
            sys.exit(0)
        else:
            sys.exit(1)

    def insert_case_res(self, test_case, report_id, build_code):
        STATUS = {
                        0: u'通过',
                        1: u'失败',
                        2: u'错误',
                    }
        for (n, t) in test_case:
            case_name = t.id()
            # a = t.shortDescription()
            # b = t._testMethodDoc
            case_doc = t._testMethodDoc or ""
            case_doc = case_doc.replace(" ", "").replace("：", ":").split('\n') or []
            cn_name = ""
            creater = ""
            for i in case_doc:
                if "用例名" in i and ":" in i:
                    cn_name = i.split(':')[1]
                    continue
                if "创建人" in i and ":" in i:
                    creater = i.split(':')[1]
                    # continue
            status = STATUS[n]

            insert_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = f"""
                        INSERT INTO tapd.auto_ui_case (
                        case_name,
                        cn_name,
                        creater,
                        report_id,
                        insert_time,
                        build_code,
                        run_res
                    )
                    VALUES
                        (
                         '{case_name}',
                         '{cn_name}',
                         '{creater}',
                         '{report_id}',
                         '{insert_time}',
                         '{build_code}',
                         '{status}' 
                        );
                        """
            self.m.insertDB(sql)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--case_dir", default="test_case", help='用例路径，根目录不用写')
    parser.add_argument("--env", default="itest", help='执行环境')
    parser.add_argument("--debug", default=1, help='debug不保存结果到数据库')
    parser.add_argument("--headless", default=False, help='无界面运行')
    parser.add_argument("--build", default=["", "", ""], nargs='+', help='按顺序填写,空格分开，顺序不能乱：构建名称 构建编号 迭代名称')
    args = parser.parse_args()
    param = vars(args)
    print(param["debug"])
    Main().run(param)
