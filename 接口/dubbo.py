#coding=utf-8
import dubbo_telnet
import json
# 初始化dubbo对象
def cdubbo(Host,Port,interface,method,params):
    try:
        conn = dubbo_telnet.connect(Host, Port)
        # 设置telnet连接超时时间
        conn.set_connect_timeout(10)
        # 设置dubbo服务返回响应的编码
        conn.set_encoding('gbk')
        # 显示服务列表
        # print "打印服务列表名："
        # print conn.do("ls")
        # 显示指定服务的方法列表
        # print "打印方法名："
        # print conn.do("ls %s"%(interface))
        conn.invoke(interface,method,params)
        # print (param)
        result = 'invoke %s.%s(%s)'%(interface,method,params)
        # print json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '), skipkeys=True, ensure_ascii=False)
        return conn.do(result)
    except:
        return Exception
if __name__ == '__main__':
    Host = '192.168.3.47' # Doubble服务器IP
    Port = '34889'  # Doubble服务端口
    interface = 'com.erp.remote.main.dubbo.service.ISskService'#'com.erp.remote.service.IHappyFundService'
   
    method = 'findRzqdByWorkerId'
    param = {}
    param['workerId'] = '01010619'
    # param['money'] = '20'
    # param['desc'] = '123456'
    # param['zrWorkerId'] = '01010528'
    param['roleId'] = '80'
    print  (param)
    params = json.dumps(param)
    print (params)
    data = cdubbo(Host, Port, interface, method, params)
    print (data)
    print (u'\u53c2\u6570\u4e0d\u5b8c\u6574')

