# -*- coding:utf-8 -*-
from PIL import Image
import pytesseract
import requests
import base64
from aip import AipOcr

class ImageShow:
    def __init__(self, address, data):
        self.url = address
        self.data = data
        self.session = requests.session()
        self.header = {"imei": "867464036577179", "methodCode": "50018", "serviceCode": "40001", "v": "7",
                       "appName": "android-ssk"}
        self.imageName = "a.png"
        self.APP_ID = "16230779"
        self.API_KEY = "xerzP5jMVzvnw45tYcjT6TvE"
        self.SECRET_KEY = "dKXrk7pnQXYqLIu5i1g5KKSGGVWlRR8r"
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)  # 初始化百度APT

    # 获取接口返回的base64字符
    def get_code(self):
        result = self.session.post(self.url, data=self.data, headers=self.header).json()
        if str(result['success']) == 'True':
            checkCodeUrl = result['data']['data']['checkCodeUrl']
            return base64.b64decode(checkCodeUrl)
        else:
            raise Exception

    # 获取验证码图片
    def get_Image(self):
        try:
            with open(self.imageName, "wb") as f:
                f.write(self.get_code())
                f.flush()
                f.close()
        except:
            raise Exception
        # print self.code_Text()

    def code_Text(self):
        rep = {'O': '0', 'I': '1', 'L': '1', 'Z': '2', 'S': '8', ' ': ''}
        qq = Image.open(self.imageName)
        text = pytesseract.image_to_string(qq, config='--psm 7').strip()
        for r in rep:
            text = text.replace(r, rep[r])
        return text

    # 获取图片内容
    def get_file_content(self):
        with open(self.imageName, 'rb') as fp:
            return fp.read()

    # 通过百度ORC识别验证码
    def get_image_code(self):
        self.get_Image()
        image = self.get_file_content()
        res = self.client.basicAccurate(image)
        print (res['words_result'][0]['words'])

if __name__ == '__main__':
    url = "http://172.16.3.100/aicp/mainremote"
    show = ImageShow(url, "msgBody={}&methodCode=50018")
    show.get_image_code()
