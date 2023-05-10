#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/5/10 9:46
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import requests,json

def get_access_token():
    """
    生成鉴权签名（Access Token）
    """
    API_KEY = "SM5q5KG23iKOGXpcu2GXQ4We"
    SECRET_KEY = "xkGaPAnzRZbcSrjmndmUMIGfLooo0or6"
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


class Sensitive():


    def __init__(self):
        self.access_token = get_access_token()


    def get_info(self,text):
        url = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined?access_token=" + self.access_token

        payload = 'text=%s'%text
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload.encode()).text
        # print(response)
        a = json.loads(response)
        b = self.check(a)
        return b


    def check(self,a):
        try:
            if a['conclusion'] == '合规':
                pass
                print('文字内容未发现违规')
            elif a['conclusion'] == '不合规':
                for i in a['data']:
                    print('检测到违规文字:%s,%s'%(i['hits'][0]['words'],i['msg']))
            else:
                print('敏感词校验失败')
        except:
            print('敏感词校验失败')



if __name__ == '__main__':
    text = '他家的的不好'
    p = Sensitive()
    print(p.get_info(text))
