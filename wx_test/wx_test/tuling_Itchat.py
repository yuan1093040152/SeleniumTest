 #-*- coding:utf-8 -*-
import itchat
import requests

def get_response(msg):
    # 改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        # 图灵 Key
        'key': '9da6f0e3dea044559ee1efb04aa02840',
        # 这是我们发出去的消息
        'info': msg,
        # 这里你想改什么都可以
        'userid': 'wechat-robot',
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    # print r.get('text')
    return r.get('text')


#好友
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    # print "name=",msg
    # 打印好友给你发了什么消息
    print "好友消息：",  msg['Text']
    # 打印机器人回复的消息
    type = get_response(msg['Text'])
    print "机器人回复：", type
    return type


#群聊
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def print_content(msg):
    # print "group=",msg
    # 打印哪个群的好友给你发了什么消息
    print "群内消息", msg["ActualNickName"] + ":" + msg['Text']
    # try:
    # 这里可以在后面加更多的or msg["ActualNickName"]=='你希望自动回复群中谁的消息   （填备注）
    if msg["ActualNickName"]==u'丽丽' or msg["ActualNickName"]==u'维维' or msg["ActualNickName"]=='Test-wechat1':
        type = get_response(msg['Text'])
        # 打印机器人回复的消息
        print "机器人回复：",type
        return type
    else:
        # 其他群聊直接忽略
        pass
    # except:
    #     pass


itchat.auto_login(True)
itchat.run()