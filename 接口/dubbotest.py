#-*- coding: utf-8 -*-

import dubbo_telnet
import json
Host = '192.168.1.204'  # Doubble服务器IP
Port = '28364'  # Doubble服务端口

# 初始化dubbo对象
conn = dubbo_telnet.connect(Host, Port)

# 设置telnet连接超时时间
conn.set_connect_timeout(10)

# 设置dubbo服务返回响应的编码
conn.set_encoding('gbk')

# 显示服务列表
print (conn.do("ls"))

# 显示指定服务的方法列表
# print conn.do("ls XXXService")

# 方法调用
# interface = 'XXXService'
# method = 'userinfo'
# param = user_id
# result = conn.invoke(interface, method, param)

# print json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '), skipkeys=True, ensure_ascii=False)