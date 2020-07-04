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
        # print (conn.do("ls"))
        # # 显示指定服务的方法列表
        # # print "打印方法名："
        # print (conn.do("ls %s"%(interface)))
        conn.invoke(interface,method,params)
        # print (param)
        result = 'invoke %s.%s(%s)'%(interface,method,params)
        # print json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '), skipkeys=True, ensure_ascii=False)
        return conn.do(result)
    except:
        return Exception
if __name__ == '__main__':
    Host = '172.16.7.47' # Doubble服务器提供者IP
    Port = '28364'  # Doubble服务提供者端口
    interface = 'com.erp.remote.cs.ICustomerRemoteService'#'com.erp.remote.service.IHappyFundService'
   
    method = 'lockCustomer'
    param = {}
    param['csTel'] = '1818181'
    param['customerId'] = '26b7dded-1dd0-43d2-b9f9-1744947d8b58'
    param['remark'] = '123456'
    param['channel'] = '4'
    # param['roleId'] = '80'
    print  (param)
    params = json.dumps(param)
    print (params)
    data = cdubbo(Host, Port, interface, method, params)
    print (data)
    

