#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/6/13 9:21
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import requests
import json,os


class AI_paint:

    def __init__(self):
        self.API_KEY = "YkrPkujMQglreKdlSDxNX7qI"
        self.SECRET_KEY = "mFj8UeB9qVtiVhrtznwkGcIszMLxmRFi"
        self.prompt = os.environ['prompt']
        self.image_num = os.environ['image_num']
        self.width = os.environ['width']
        self.height = os.environ['height']
        #调试
        # self.prompt = "萌，闪亮，完美，超高清，金色双马尾，金色月亮头饰，面容精致，详细刻画身体，人像居中，看镜头"
        # self.image_num =1
        # self.width =1024
        # self.height =1024



    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))


    def paint(self):
        url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/txt2imgv2?access_token="+ self.get_access_token()
        # image 可以通过 get_file_content_as_base64("C:\fakepath\350X150.png",False) 方法获取
        payload = json.dumps({
            "prompt": self.prompt,
            "version": "v2",
            "width": self.width,
            "height": self.height,
            "image_num": self.image_num
        })
        print(payload)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).text
        print(type(response))
        print(response)
        load = json.loads(response)
        rep = load["data"]["task_id"]
        print(rep)
        return rep

    #获取链接
    def main(seif):
        url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/getImgv2?access_token=" + seif.get_access_token()

        payload = json.dumps({
            "task_id": seif.paint()
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).text
        load = json.loads(response)
        print(type(load))
        print(load)

        for i in load["data"]["sub_task_result_list"]:
            print(i["final_image_list"][0]["img_url"])






if __name__ == '__main__':
    AI_paint().paint()
