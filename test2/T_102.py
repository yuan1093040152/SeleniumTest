# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=I9wVxfAuVi33gXTKdZ6lGxP3&client_secret=QasLDoIORbV52GPZZOwvv8GSNsCTXwti'
# response = requests.get(host)
# if response:
#     print(response.json())


"""
    {u'access_token': u'24.cae9f104d3d5c8590660784451e5b766.2592000.1597549661.282335-21435272', u'expires_in': 2592000, u'session_secret': u'897a3b52f6896698ebbda0b2526788e1', 
    u'scope': u'public brain_all_scope brain_colourize brain_stretch_restore brain_dehaze brain_contrast_enhance 
    brain_image_quality_enhance brain_style_trans brain_image_definition_enhance brain_selfie_anime wise_adapt 
    lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 
    vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app 
    smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi 
    fake_face_detect_\u5f00\u653eScope vis-ocr_\u865a\u62df\u4eba\u7269\u52a9\u7406 idl-video_\u865a\u62df\u4eba\u7269\u52a9\u7406', 
    u'session_key': u'9mzdWBGYpkYaHVROrvxvDGtwKebh1tpCKm1Y64EY3VSONSPsBivYCZIhXIgsCZ5EHNPXy6vJ7mtLMdOLYUeisYb7fUqXNg==', 
    u'refresh_token': u'25.9050ba5491d6bccbc7f1f692d68c6ac0.315360000.1910317661.282335-21435272'}
"""


import base64


#黑白图像上色
# request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/colourize"

#人像动漫化
request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"

# 二进制方式打开图片文件
f = open('E:\\test\\234.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.cae9f104d3d5c8590660784451e5b766.2592000.1597549661.282335-21435272'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:

    print (response.json())
    data = response.json()
    print(data)
    img_str = data['image']
    #图片base64编码保存图片
    img_data = base64.b64decode(img_str)
    with open('E:\\test\\121237.jpg', 'wb') as f:
        f.write(img_data)


