#coding=utf-8
import itchat
import requests
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 抓取网页
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', 'Picture'],isFriendChat=True)
def text_reply(msg):
    print msg
    # 当消息不是由自己发出的时候
    # if not msg['FromUserName'] == Name["Jestiao"]:
    # 回复给好友
    apikey = '9da6f0e3dea044559ee1efb04aa02840'
    url = "http://www.tuling123.com/openapi/api?key="+str(apikey)+"&info="
    url = url + msg['Text']
    html = getHtmlText(url)

    message = re.findall(r'\"text\"\:\".*?\"', html)

    reply = eval(message[0].split(':')[1])
    print reply ,'[]'
    return reply



@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)    #群消息的处理
def print_content(msg):
    print msg
    print (msg.User["NickName"])
    if msg.User["NickName"]==u'测试测试' or msg.User["NickName"]==u'尼古拉斯':    #这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字'
        print(msg.User['NickName'] +":"+ msg['Text'])     #打印哪个群给你发了什么消息
        print(text_reply(msg['Text'])+"\n")           #打印机器人回复的消息
        return text_reply(msg['Text'])
    else:                                         #其他群聊直接忽略
        pass


if __name__ == '__main__':
    # 扫码登陆微信
    itchat.auto_login()
    # 获取自己的UserName
    # friends = itchat.get_friends(update=True)[0:]
    # #  使用字典存放好友昵称与用户名
    # Name = {}
    # # 好友昵称
    # Nic = []
    # # 好友用户名
    # User1 = []
    # for i in range(len(friends)):
    #     Nic.append(friends[i]["NickName"])
    #     User1.append(friends[i]["UserName"])
    # for i in range(len(friends)):
    #     Name[Nic[i]] = User1[i]
    itchat.run()