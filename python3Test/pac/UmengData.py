#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/9/9 11:35
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import requests,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


 #判断运行浏览器
def open_browser(browser,url):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        pass
    driver.get(url)
    return driver

class UmengAfter():

    def __init__(self,browser,url):
        self.browser = open_browser(browser, url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)

    # 输入
    def ImputElement(self, type, element, value):
        self.browser.find_element(by=type, value=element).send_keys(value)

    # 清除
    def CleanElement(self, type, element):
        self.browser.find_element(by=type, value=element).clear()

    # 点击
    def ClickElement(self, type, element):
        self.browser.find_element(by=type, value=element).click()

    # 获取
    def GetElement(self,type, element):
        self.browser.find_element(by=type, value=element)

    # 关闭窗口
    def Close(self):
        self.browser.close()

    # 关闭浏览器
    def Quit(self):
        self.browser.quit()

    # 时间
    def Time(self, s):
        time.sleep(s)

    # 等待
    def Wait(self, s):
        self.browser.implicitly_wait(s)

    def get_tracks(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance:偏移量
        :return:移动轨迹
        """
        # 移动轨迹
        tracks = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 5
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            tracks.append(round(move))
        return tracks

    def move_to_gap(self, slider, tracks):
        """
        拖动滑块
        :param slider: 滑块
        :param tracks: 轨迹
        :return:
        """
        # 模拟滑动滑块
        action = ActionChains(self.browser)
        action.click_and_hold(slider).perform()
        # action.reset_actions()   # 清除之前的action
        for i in tracks:
            action.move_by_offset(xoffset=i, yoffset=0).perform()
        time.sleep(0.5)
        action.release().perform()



    #登录
    def login(self,uesr,pwd):
        #ifame和伪元素定位
        self.browser.switch_to.frame('alibaba-login-box')
        self.ImputElement(By.ID,'fm-login-id',uesr)
        self.ImputElement(By.ID, 'fm-login-password', pwd)
        self.Time(2)
        self.ClickElement(By.ID,'fm-login-submit')
        self.Time(2)

        # ifame和伪元素定位
        self.browser.switch_to.frame('baxia-dialog-content')
        self.Time(1)

        #滑动的滑块
        # huakuai = self.GetElement(By.ID,'nc_1_n1z')
        huakuai = self.browser.find_element_by_css_selector('span#nc_1_n1z.nc_iconfont.btn_slide')
        a = huakuai.location['x']
        print(a)

        #定义
        action = ActionChains(self.browser)
        #鼠标点击滑动块不松开
        action.click_and_hold(huakuai).perform()
        #将滑块右滑动至相对起点位置的xoffset点
        action.move_by_offset(xoffset=207, yoffset=0).perform()
        self.Time(5)
        # 放开滑块
        action.release(huakuai).perform()
        self.Time(2)
        self.Close()
        self.Quit()









if __name__ == '__main__':
    browser = 'Chrome'
    url = 'https://passport.umeng.com/login?redirectURL=https%3A%2F%2Fapm.umeng.com%2Fapps%2Flist'
    user = '1918288888@qq.com'
    pwd = '2017_gh=jjs'
    p = UmengAfter(browser,url)
    p.login(user,pwd)




"""
Hm_lvt_289016bc8d714b0144dc729f1f2ddc0d=1631158249; 
UM_distinctid=17bc89ba882785-0ca0dabf1509b5-3f3a5d0e-1fa400-17bc89ba88377d; 
dplus_cross_id=17bc89ba884121-015e11ab567954-3f3a5d0e-1fa400-17bc89ba885826; 
dplus_finger_print=3629742979; 
cna=7fd4fa2193f34ec29182f63b20ccc6b1; 
uc_session_id=d9204b40-e213-45e6-9f49-d8db0184af6d; 
arms_uid=dea2a846-abe8-45a1-bf3d-6f1bfe245f1d; 
CNZZDATA1259864772=1942959023-1631155605-%7C1631166406; 
umplus_uc_token=1idWzBDudVceWy326xoY8EQ_256c1ca9760a4169a58b73add451f53c; 
umplus_uc_loginid=1918288888%40qq.com; 
cn_1258498910_dplus=1%5B%7B%22common_is_lt_ie8%22%3A%22N%22%2C%22common_is_spider_hit%22%3A%22N%22%7D%2C0%2C1631166493%2C0%2C1631166493%2Cnull%2C%2217bc89ba882785-0ca0dabf1509b5-3f3a5d0e-1fa400-17bc89ba88377d%22%2C%221631154208%22%2C%22https%3A%2F%2Fapm.umeng.com%2F%22%2C%22apm.umeng.com%22%5D; EGG_SESS=Z8T-GQGU9dF1c3E3Owi-bHQMZc6QjJvfIEK0rFWeR_V45Gt_iyzFkytoJoUumlbNeIfLNJt1ujUq9Tj-Ue8ZEpSDln9eJOuJqw5JPQdlN_bmhRV0ECVcwOKHmcJRtEaxoWFxLXXObQzKQrZfgQedhOIg5ZyXAQn-Fza7Dui6bTV3wpF8zvBVJQ0FerqjTjZFakgsS0n5ea1k4ufShYT8uhcXFiT7Cf6vbmSrI4nML9oV3x9yTF5vw56yMY1KPM-frgfMYaENUcPdIbASDWib8fEmQig75YLUATMY7ieKdYhJvvcglYZc-FFFnsc20Pungf_TvhlmPXM2JAd6cCoJZxbxJrraNkyr2drezqpNZYv8xHXta8fhsWtC6p6jiIQcry2_wabvCVcJsr1ZpZe5Uu_wAblkCV-Y0CSu0pzPIffH3wA75c0b6e3bBm93sIyVOdqHYNU1D_qgJlgQGbc7P02IeVejrB86c1Rw_DQ7wyNSWwVVbZGx67z9oTVZWnt-wAJr9niXlrRuPCwvPHdnTJhRrmwzUEj1KOAuUqEjoYpyQxYZNoetMvGauE8sKpBtua4JYOko9OWIZUoatl-pe8xYrN52VAZp7kA_JQ2WO8ifYquWEwQPGB-siFzISg1z7KlnyiQ_oMBkK0B1J7uBdKt38dCK8Rtm1ByhUQiylwgQ5AkiyDqcsByjTeBly7StM9rXjFo1utuRQ7izfUEV-yf7965Lran3Z0F3hF7T_l3Tv6QncKBkcVcpU0bXmNtekYdlBvSCRozvcHIsEq5L6Q==; 
PHPSESSID=bler97q7apl3hn3i9a876gg5a0; 
Hm_lpvt_289016bc8d714b0144dc729f1f2ddc0d=1631168125; 
cn_1259864772_dplus=1%5B%7B%22common_is_lt_ie8%22%3A%22N%22%2C%22common_is_spider_hit%22%3A%22N%22%2C%22UserID%22%3A%221918288888%40qq.com%22%7D%2C0%2C1631168195%2C0%2C1631168195%2C%22%24direct%22%2C%2217bc89ba882785-0ca0dabf1509b5-3f3a5d0e-1fa400-17bc89ba88377d%22%2C%221631155605%22%2C%22%24direct%22%2C%22%24direct%22%5D

"""


