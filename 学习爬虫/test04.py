# coding=utf-8
import wx

app = wx.App()
window = wx.Frame(None, title = "wxPython - www.yiib.com", size = (300,300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label = u"东哥你个傻X", pos = (100,100))
window.Show(True)
app.MainLoop()



