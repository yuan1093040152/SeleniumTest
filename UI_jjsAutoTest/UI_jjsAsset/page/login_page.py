#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/10 14:30
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import time
from UI_jjsAutoTest.UI_jjsAsset.page.base_page import BasePage
from UI_jjsAutoTest.UI_jjsAsset.lib import read_config
from selenium.webdriver.common.by import By
from PIL import Image
from aip import AipOcr
import time


class LoginPage(BasePage):
    login_controls = {
        "username": "css=>.inputUserName",
        "password": "css=>.inputPassword",
        "login_button": "class=>loginBtn",
        "check":"css=>a[href='/v/zdhb/list']",
        "login_check":"xpath=>.//*[text()='退出']",
        "close_popup": "xpath=>.//*[text()='取消']",
        "aui_close": "class=>aui_close",
        "code":"id=>ckNum",
        "errorArea":"id=>errorArea",
        "verify_code":"id=>verify_code"
    }

    # itest环境登录
    def itestlogin(self):
        time.sleep(2)
        self.d.send_key(self.login_controls["username"], self.itestempno)
        self.d.send_key(self.login_controls["password"], self.itestpassword)
        self.d.click(self.login_controls["login_button"])
        print('已登录新系统')
        try:
            # p.ClickElement(By.CLASS_NAME,'aui_close')
            self.d.click(self.login_controls["aui_close"])
        except:
            print('没有弹窗跳过')
        time.sleep(2)


    # 线上环境登录
    def ilogin(self):
        time.sleep(2)
        self.d.send_key(self.login_controls["username"], self.iempno)
        self.d.send_key(self.login_controls["password"], self.ipassword)

        for i in range(10):
            a = i + 1
            # q.CleanElement(By.ID, 'ckNum')
            self.d.send_key(self.login_controls["code"],self.getcode())
            self.d.click(self.login_controls["login_button"])
            # q.ImputElement(By.ID, 'ckNum', self.getcode(q))
            # q.ClickElement(By.ID, 'login_button')
            time.sleep(1)

            try:
                info = self.d.get_text(self.login_controls["errorArea"])
                # info = q.browser.find_element(By.ID, 'errorArea').text
                print(info)
                if info == '请输入正确的验证码！':
                    print('验证码识别错误，第%d次重试' % a)
                else:
                    print('验证码识别成功')
                    break

            except Exception as e:
                print(e)
                print('登录成功！')
                break


    def login_check(self, name):

        return self.d.wait_and_save_exception(self.login_controls["login_check"], name)

    def close(self):
        self.d.click(self.login_controls["close_popup"])

    # 通过元素获取验证码
    def getcode(self):
        # 方法一：通过元素获取验证码
        path = '123.png'
        path1 = '1234.png'
        # 截图整个页面
        self.d.driver.save_screenshot(path)
        # q.browser.save_screenshot(path)
        # 获取元素的坐标（x为上，y为左，w为下，h为右，减为上移，加为下移）
        img1 = self.d.driver.find_element_by_id(self.login_controls["verify_code"])
        # img1 = q.browser.find_element(By.ID, 'verify_code')
        left = img1.location['x'] - 20
        top = img1.location['y'] - 20
        Width = left + img1.size['width'] + 30
        Height = top + img1.size['height'] + 30
        print(left, top, Width, Height)
        picture = Image.open(path)
        # 根据上面的元素坐标裁剪图片
        picture = picture.crop((left, top, Width, Height))
        picture.save(path1)

        # 方法二：通过链接获取验证码
        # 获取元素中src的链接
        # img = self.browser.find_element(By.ID,'verify_code').get_attribute('src')
        # print(img)
        # r = requests.get(img)
        # with open(path1,'wb') as f:
        #     f.write(r.content)

        # 百度高精度识别https://ai.baidu.com/ai-doc/OCR/1k3h7y3db
        APP_ID = read_config.read_config('ocr', 'APP_ID')
        API_KEY = read_config.read_config('ocr', 'API_KEY')
        SECRET_KEY = read_config.read_config('ocr', 'SECRET_KEY')

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        with open(path1, 'rb') as f:
            image = f.read()
        image1 = client.basicAccurate(image)
        print(image1)
        return image1['words_result'][0]['words']



