#coding=utf-8
from wxpy import *
import json,requests

#缓存自动登陆
# bot = Bot()
bot = Bot(cache_path=True)

#获取聊天对象（群聊）
#注：如果获取不到群聊，请将群聊保存到通讯录
# group = bot.groups().search(u'尼古拉斯')[0]
# print (group)

#获取聊天对象（好友）
friend = bot.friends().search('Test-wechat')[0]
print (friend)

#发送文本
# group_info = group.send('1')

#发送图片
# friend_info = friend.send_image('timg.jpg')
friend_info = friend.send(u'你好')

#以动态的形式发送图片
# friend_info1 = friend.send('@img@timg.jpg')

#发送视频
# friend_info2 = friend.send_video('xxx.mp4')

#发送文件
# friend_info3 = friend.send_file('xxx.zip')

#发送文件给传输助手
# friend_info4 = bot.file_helper.send('1')

#获取微信好友数据
# data = bot.friends().stats_text()
# print (data)





def auto_ai(text):
    apikey = '9da6f0e3dea044559ee1efb04aa02840'
    # response = getHtml(request.encode('utf-8'))
    keyword = 'f054462bf5248d36'
    url = 'http://openapi.tuling123.com/openapi/api'
    # url1 = 'http://www.tuling123.com/openapi/api'
    # payload={
    #     "key":apikey,
    #     "info":text,
    #     "userid":442814
    #     }

    payload ={
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": apikey,
            "userId": 442814
        }
    }

    # print (1)
    r = requests.post(url,data=json.dumps(payload))
    # print (r)
    # print (r.content)
    # print (type(r.content))
    result1 = json.loads(r.content)
    # result = r.content['text']
    # return result['text']
    # print (type(result))
    print (result1)
    result = result1['results'][0]['values']
    print (u'机器人回复:'+result['text'])
    # print (u'机器人回复:' + result['code'])
    # return result['text']
    # print (result)
    if ('url' in result.keys()):
        return u'机器人回复:'+result['text']+result['url']
    else:
        return u'机器人回复:'+result['text']



print (u'机器人已启动')

#激活监听事件，自动回复 不填参代表回复所有人，填参代表回复指定人
@bot.register(friend)
def group_msg(msg):
    print (u'接收消息：'+str(msg))
    print (type(msg))
    if (msg.type != 'Text'):
        print (2)
        ret = u'[奸笑][奸笑]'
        # return ret
    else:
        print (1)
        ret = auto_ai(msg.text)
        # return ret
    return ret





embed()