#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/2/22 20:09
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import openai,time,argparse

openai.api_key = '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'

def Completion(text):
    completion = openai.Completion.create(
        #text-davinci-002  会分析题目
        #text-davinci-003  只会给答案

        engine = "text-davinci-003",
        prompt = text,
        max_tokens = 512,
        temperature = 0.5
    )
    return completion


if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # 获取jenkins传递过来的参数
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()
    param = vars(args)
    text = param['text']

    #测试
    # text ='1+1=?'

    print("问：\n",text,'\n')
    re = Completion(text).choices[0].text

    print("答：%s" % re)

