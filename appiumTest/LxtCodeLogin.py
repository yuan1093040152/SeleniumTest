#coding=utf-8
from appium import webdriver
from PIL import Image
from aip import AipOcr
from AppiumLibrary import *
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')



class LxtCodeLogin(AppiumLibrary):
    # desired_caps = {}
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '6.0.1'
    # desired_caps['deviceName'] = 'OPPO R9s'
    # desired_caps['appPackage'] = 'com.jjshome.optionalexam'
    # desired_caps['appActivity'] = 'com.jjshome.optionalexam.ui.main.WelcomeActivity'  # 乐学堂的activity
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # driver.implicitly_wait(10)

    #百度ID KEY
    def demo(self):
        APP_ID = '16947930'
        API_KEY = '0ynD0BGPC6QtrPWs68i4sQO9'
        SECRET_KEY = 'fKsckEf41jUtTDBwFIeHYkhnYyvNaViz'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        return client

    #读取图片
    def get_file_content(self,filePath):
        with open(str(filePath), 'rb') as f:
            return f.read()

    #调用百度ORC高精度识别验证码
    def get_image_code(self,filePath):
        image = self.get_file_content(self)
        client = self.demo()
        image1 = client.basicAccurate(image)
        print image1
        return image1['words_result'][0]['words']

    def code(self):
        self.find_element_by_id('btn_securityCode').click()   #点击获取验证码
        time.sleep(3)
        self.driver.find_element_by_class_name('android.widget.ImageView').click()  # 点图标隐藏键盘
        self.driver.get_screenshot_as_file(r'D:\\a.png')
        Element = self.driver.find_element_by_id('img_code')
        LeftUpper = int(Element.location['x'])
        LeftLower = int(Element.location['y'])
        RightUpper = int(Element.location['x']+Element.size['width'])
        lowerRight = int(Element.location['y']+Element.size['height'])
        img = Image.open(r'D:\\a.png')
        img = img.crop((LeftUpper,LeftLower,RightUpper,lowerRight))
        self.filePath = r'D:\\b.png'
        imgPath = img.save(self.filePath)
        return self.filePath

    def login(self):
        print (1)
        try:
            self.driver.find_element_by_id('tv_input').click()
        except :
            pass
        print (2)
        filePath = self.code()
        DemoCode = self.get_image_code(filePath)
        print (DemoCode)
        self.driver.find_element_by_id('et_securitycode').send_keys(DemoCode)
        self.driver.find_element_by_class_name('android.widget.ImageView').click()   #点图标隐藏键盘
        self.driver.find_element_by_id('et_workerno').send_keys('252613')
        self.driver.find_element_by_id('et_password').send_keys('mm711232')
        self.driver.find_element_by_class_name('android.widget.ImageView').click()  # 点图标隐藏键盘
        self.driver.find_element_by_id('bt_login').click()
        time.sleep(10)

        # driver.quit()


if __name__ == '__main__':
    LxtCodeLogin()