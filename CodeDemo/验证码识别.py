from PIL import Image
import pytesseract
from selenium import webdriver
import time
url='http://i.jjshome.com'
driver = webdriver.Chrome()
driver.maximize_window()   
driver.get(url)
time.sleep(3)
driver.save_screenshot('e://aa.png')  
imgelement = driver.find_element_by_xpath('//*[@id="verify_code"]')   
location = imgelement.location   
size=imgelement.size  
rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) 
i=Image.open("e://aa.png")  
frame4=i.crop(rangle)  
frame4.save('e://frame4.jpg')
qq=Image.open('e://frame4.jpg')
text=pytesseract.image_to_string(qq).strip()
print text
