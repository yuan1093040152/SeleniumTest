#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/10 14:07
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


# coding=utf-8
import logging

from selenium import webdriver
from UI_jjsAutoTest.UI_jjsAsset.lib.path import DRIVER_PATH
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import win32api,win32con
import time


class Base(object):

    def __init__(self, browser='ff'):

        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            option = webdriver.ChromeOptions()
            option.add_argument("--start-maximized")
            driver = webdriver.Chrome(DRIVER_PATH)
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        elif browser == 'edge':
            driver = webdriver.Edge()
        try:
            self.driver = driver
        except Exception:
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)

    def element_wait(self, css, secs=10):
        '''
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif by == "partialLinktext":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        elif by == "tag_name":
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.TAG_NAME, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self, css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")
        style = "border: 2px solid green;"
        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            element = self.driver.find_element_by_id(value)
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element,style)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);" ,element ,style)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);" ,element ,style)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);" ,element ,style)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);" ,element ,style)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);" ,element ,style)
        elif by == "tag_name":
            element = self.driver.find_element_by_tag_name(value)
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);" ,element ,style)


        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        '''
        Usage:
        driver.open("http://www.itest.leyoujia.com")
        '''
        self.driver.get(url)

    def max_window(self):
        '''
        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.
        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def send_key(self, css, text):
        '''
        Operation input box.

        Usage:
        driver.send_key("css=>#el","selenium")
        '''
        logging.info("======开始执行======%s"%css)
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.click()

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, css):
        '''
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def add_attribute(self, css, attributeName, value):
        self.driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, css, value)

        # self.driver.get(url)
        # element = self.driver.find_element_by_xpath('//input')
        # 向页面文本框input标签中添加新属性name='search'
        # addAttribute(self.driver, element, 'name', 'search')
    # def add_attribute(driver, elementobj, attributeName, value):
    #     '''
    #     封装向页面标签添加新属性的方法
    #     调用JS给页面标签添加新属性，arguments[0]~arguments[2]分别
    #     会用后面的element，attributeName和value参数进行替换
    #     添加新属性的JS代码语法为：element.attributeName=value
    #     比如input.name='test'
    #     '''
    #     driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, elementobj, value)


    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()


    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to.default_content()

    def open_new_window(self, css):

        original_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])

    def switch_window(self, index):
        # 根据输入的标签页序号切换到任意标签页
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    def wait_and_save_exception(self, css, name):
        try:
            self.element_wait(css, secs=5)
            return True
        except Exception as e:
            from lib.path import WEBPICTUREPATH
            self.get_windows_img(WEBPICTUREPATH + name + '.jpg')
            return False

    def wait_and_exception(self, css):
        try:
            self.element_wait(css, secs=10)
            return True
        except Exception as e:
            return False

    def select_by_value(self, css, value):
        self.element_wait(css)
        el = self.get_element(css)
        Select(el).select_by_value(value)

    def isElementExist(self, css, value):
        self.element_wait(css)
        el = self.get_element(css)
        Select(el).select_by_value(value)

    def is_Element_Exist(self, css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")
        style = "border: 2px solid green;"
        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            try:
                self.driver.find_element_by_id(value)
                return True
            except:
                return False

        if by == "xpath":
            try:
                self.driver.find_element_by_xpath(value)
                return True
            except:
                return False

    def get_windows_count(self):
        all_handles = self.driver.window_handles
        return len(all_handles)


    def is_visible(self, css, secs=10):
        '''
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
        elif by == "partialLinktext":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        elif by == "tag_name":
            WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.TAG_NAME, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")


    def is_not_visible(self, css, secs=20):
        '''
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
        elif by == "partialLinktext":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        elif by == "tag_name":
            WebDriverWait(self.driver, secs).until_not(EC.visibility_of_element_located((By.TAG_NAME, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")


    def GetCursorPos(self):
        '''获取当前鼠标位置'''
        pos = win32api.GetCursorPos()
        return int(pos[0]),int(pos[1])

    def SetCursorPos(self,x,y):
        '''获取当前鼠标位置'''
        win32api.SetCursorPos((x,y))


    def drag_and_drop_new(self,css_s,scc_e,x_py=10,y_py=10):
        self.element_wait(css_s)
        start = self.get_element(css_s).location
        end = self.get_element(scc_e).location
        panel_height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
        start_x=start['x']  + x_py
        start_y=start['y']+ panel_height + y_py
        end_x=end['x'] + x_py
        end_y=end['y'] + panel_height + y_py
        move_x =  end_x - start_x
        move_y =  end_y - start_y
        print (start_x,start_y)
        print (move_x,move_y)
        print (end_x,end_y)
        win32api.SetCursorPos((start_x,start_y))
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,start_x,start_y)
        # time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,move_x,move_y)
        win32api.SetCursorPos((end_x, end_y))
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



    def drag_and_drop_new1(self):
        win32api.SetCursorPos((482,303))
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,482,303)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,917,166)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


if __name__ == '__main__':
    driver = Base("chrome")
