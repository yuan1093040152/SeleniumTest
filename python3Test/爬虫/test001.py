#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/8/11 18:39
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


a = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 201
Content-Type: application/json; charset=UTF-8
"""


#替换
b = a.replace('\n','!')

# print(b)
c = a.split('\n')
print(c)

e = []
for d in c:
    if len(d)==0:
        pass
    else:
      e.append(d)

print(e)

# d = c.remove('')
# print(d)




import win32clipboard as wc
import win32con
import sys



# def stripClipboard():
#     # 开始剪切板操作
#     wc.OpenClipboard()
#     # 尝试将剪切板内容读取为Unicode文本
#     # 如果复制的内容是文件而非文本，读取为Unicode文本会报错，所以需要错误处理。
#     try:
#         txt = wc.GetClipboardData(win32con.CF_UNICODETEXT)
#     except Exception as e:
#         print("剪切板内容非文本，无法去除换行符。")
#         wc.EmptyClipboard()
#         sys.exit("已清空剪切板并退出。")
#     txt = wc.GetClipboardData(win32con.CF_UNICODETEXT)
#     txt = str(txt).strip()
#     # 字符串按行分割
#     txt = txt.splitlines()
#     n = len(txt)
#     # 用空格拼接每行
#     txt = ' '.join(txt)
#     # 将所有长度大于1的空白符转为1个空格
#     txt = ' '.join(txt.split())
#     # 清空剪切板
#     wc.EmptyClipboard()
#     # 尝试将处理完的字符放入剪切板，注意这里用的是win32con.CF_UNICODETEXT，
#     # 如果使用win32con.CF_TEXT则需要对txt进行编码，否则会出现乱码。
#     wc.SetClipboardData(win32con.CF_UNICODETEXT, txt)
#     # 关闭剪切板
#     wc.CloseClipboard()
#     print('删除了{}个换行符\n'.format(n-1))
#    #print(txt+'\n')
#     print(txt)
#
# if __name__ == '__main__':
#     stripClipboard()