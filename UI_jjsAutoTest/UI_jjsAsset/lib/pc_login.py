#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/3 20:51
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


from UI_jjsAutoTest.UI_jjsAsset.lib import openbrowser
from selenium.webdriver.common.by import By
from PIL import Image
from aip import AipOcr
import time

class login(openbrowser.testname):

    def __init__(self):
        self.itesturl = 'http://itest.leyoujia.com/jjslogin/tologin'
        self.iurl = 'http://i.leyoujia.com/jjslogin/tologin'
        self.browser = 'Chrome'
        self.itestempno = '000012'
        self.iempno = '252613'
        self.itestpassword = '1'
        self.ipassword = 'mm711232'
        self.nowtime = time.strftime('%Y-%m-%d-%H-%M-%S')
        # self.p = openbrowser.testname(self.browser, self.itesturl)
        # self.q = openbrowser.testname(self.browser,self.iurl)


    # 通过元素获取验证码
    def getcode(self,q):
        # 方法一：通过元素获取验证码
        path = '123.png'
        path1 = '1234.png'
        # 截图整个页面
        q.browser.save_screenshot(path)
        # 获取元素的坐标（x为上，y为左，w为下，h为右，减为上移，加为下移）
        img1 = q.browser.find_element(By.ID, 'verify_code')
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
        APP_ID = '24416627'
        API_KEY = '3i88Xum6GtMrtYIYP1H8uwZ5'
        SECRET_KEY = 'D9Di9Lcon0NbOnEKTtylIGMYUshfLnyj'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        with open(path1, 'rb') as f:
            image = f.read()
        image1 = client.basicAccurate(image)
        print(image1)
        return image1['words_result'][0]['words']


    #itest环境登录
    def itestlogin(self):
        p = openbrowser.testname(self.browser, self.itesturl)
        self.Time(3)
        p.CleanElement(By.ID,'workerNo')
        p.ImputElement(By.ID,'workerNo',self.itestempno)
        p.ImputElement(By.ID, 'password', self.itestpassword)
        p.ClickElement(By.ID, 'login_button')
        print('已登录新系统')
        p.Wait(10)
        try:
            p.ClickElement(By.CLASS_NAME, 'aui_close')
        except:
            print('没有弹窗跳过')
            pass
        time.sleep(2)


    # 线上环境登录
    def ilogin(self):
        q = openbrowser.testname(self.browser, self.iurl)
        self.Time(3)
        q.CleanElement(By.ID, 'workerNo')
        q.ImputElement(By.ID, 'workerNo',self.iempno)
        q.ImputElement(By.ID, 'password', self.ipassword)

        for i in range(10):
            a = i + 1
            q.CleanElement(By.ID, 'ckNum')
            q.ImputElement(By.ID, 'ckNum', self.getcode(q))
            q.ClickElement(By.ID, 'login_button')
            time.sleep(1)

            try:
                info = q.browser.find_element(By.ID, 'errorArea').text
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
            pass




if __name__ == '__main__':

    a = login().ilogin()