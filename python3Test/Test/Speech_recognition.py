#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/12/10 10:23
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""




from aip import AipSpeech
import ffmpeg

""" 你的 APPID AK SK """
APP_ID = '23126278'
API_KEY = '2WwSaXuHjVyvfOzQjoKZ5eWB'
SECRET_KEY = 'Pc4A8PUfxecGoPwaR3HRno5cfDeePSHe'

# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# dev_pid 语言 模型 是否有标点 备注
#  1537 普通话(纯中文识别) 输入法模型 有标点 支持自定义词库
#  1737 英语 无标点 不支持自定义词库
#  1637 粤语 有标点 不支持自定义词库
#  1837 四川话 有标点 不支持自定义词库
#  1936 普通话远场 远场模型 有标点 不支持


# 读取文件
# def get_file_content(file_path):
# #     with open(file_path, 'rb') as fp:
# #         return fp.read()
# # # 识别本地文件
# # result = client.asr(get_file_content('E:/test/test01.wav'), 'wav', 16000, {
# #     'dev_pid': 1537,
# # })
# #
# # print(result)

ffmpeg.input('test01.wav').output('test02.wav',ar=16000).run()
# ffmpeg.input('test01.wav').output('test02.wav', ar=16000).run()