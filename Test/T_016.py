#coding=utf-8

'''
 AI核心代码，估值一个亿
'''


while True:
    guess = raw_input()
    txt = guess.replace('?','!')
    txt1 = txt.replace('？','!')
    txt2 = txt1.replace('吗','')
    print (txt2)

