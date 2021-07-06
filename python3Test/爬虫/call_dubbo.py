#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/7/1 14:26
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import sys
import re,requests


pythonversion=sys.version[0]
# 判断是python3则重写unicode方法
if sys.version[0]=='3':
    def unicode(s):
        # python3则转为字符串
        return str(s)

class JpClient(object):


    def IMsendinfo(self,ids, msg, moban,group='im-serve-attend',url=''):

        idsstr = ''
        # 如果是字符串则转为list
        if type(ids) != type([]):
            # ids = self.decodeUnicode(ids)
            ids = ids.replace(';', ',')
            ids = ids.replace(u'，', ',')
            ids = re.split(',', ids)
        if ids:
            for i in ids:
                idsstr = u'%s"%s",' % (idsstr, i)
            idsstr = idsstr[:-1]
            print('idsstr:',idsstr)
        else:
            return

        msg = msg.replace('\r\n', '')
        msg = msg.replace('\n', '')
        interface = 'com.jjshome.im.service.dubbo.NimAccidService'
        method = 'sendCustomMsg'
        host = '192.168.196.6'
        port = '26889'

        param = u'{"fromAccid":"servenumber000011","group":"%s","toAccids":[%s],"body":"{\\"type\\":8,\\"data\\":{\\"title\\":\\"%s\\",\\"content\\":\\"%s\\",\\"source\\":\\"im-serve-attend\\",\\"sourceName\\":\\"%s的温馨提示\\",\\"sourceType\\":\\"im-serve-fwsq\\",\\"url\\":\\"%s\\",\\"isOuterOpen\\":true}}"}' % (
            group, idsstr, moban, msg, moban, url)

        """
        {"fromAccid":"servenumber000011","group":"im-serve-attend","toAccids":["252613"],"body":"{\"type\":8,\"data\":{\"title\":\"今日未打卡提醒\",\"content\":\"今天未打卡名单：袁猛\",\"source\":\"im-serve-attend\",\"sourceName\":\"今日未打卡提醒的温馨提示\",\"sourceType\":\"im-serve-fwsq\",\"url\":\"\",\"isOuterOpen\":true}}"}

        """

        print(param)

        # param = {"fromAccid": 'servenumber000011', "toAccids": '["252613"]', "group": 'im-serve-attend',"body": '{"type":"8","data":"{"sourceName":"456","title":"567","content":"678","isOuterOpen":"true","sourceType":"im-serve-fwsq","source":"im-serve-attend","url":""}"}'}

        try:
            url = u'http://172.16.100.12:29998/netdubbo'
            data = {'host': host, 'port': port, 'method': method, 'interface': interface, 'param': param, 'code': 'gbk',
                    'outputbz': False}
            req = requests.post(url=url, data=data, timeout=5)
            print(req.text)
            print(u'调用远程服务成功。')
        except:
            print(u'乐聊通知处理出错！')


    def aa(self):
        print('{\\"type\\":8}')


"""
import com.jjshome.im.service.dubbo.NimAccidService;  -- interface
nimAccidService.sendCustomMsg(param);    -- method


Map<String, Object> param = new HashMap<>(12);
param.put("fromAccid", imNoticeSendParams.getFromAccid());
param.put("toAccids", imNoticeSendParams.getToAccids());
param.put("body", JSON.toJSONString(body)); -- 不知道是不是这个JSON的原因，body参数都需要加反斜杠
param.put("group", imNoticeSendParams.getGroup());

Map<String, Object> body = new HashMap<>(12);
body.put("data", data);
body.put("type", 8);

Map<String, Object> data = new HashMap<>(12);
data.put("sourceName", imNoticeSendParams.getSourceName());
data.put("title", imNoticeSendParams.getTitle());
data.put("content", imNoticeSendParams.getContent());
data.put("isOuterOpen", imNoticeSendParams.isOuterOpen());
data.put("sourceType", imNoticeSendParams.getSourceType());
data.put("source", imNoticeSendParams.getSource());
data.put("url", imNoticeSendParams.getUrl());



param = {"fromAccid":"servenumber000011","group":"im-serve-attend","toAccids":["252613"],"body":"{\"type\":8,\"data\":{\"title\":\"今日未打卡提醒\",\"content\":\"今天未打卡名单：袁猛\",\"source\":\"im-serve-attend\",\"sourceName\":\"今日未打卡提醒的温馨提示\",\"sourceType\":\"im-serve-fwsq\",\"url\":\"\",\"isOuterOpen\":true}}"}

"""





if __name__ == '__main__':
    ids = ["252613"]
    msg = '今天未打卡名单：袁猛'
    moban = '今日未打卡提醒'
    s = JpClient().IMsendinfo(ids, msg, moban,group='im-serve-attend',url='')
    # a = JpClient().aa()

    # s = JpClient().netleliaoTongzhi(ids=['252613','249279'], msg='abcdefg', moban=u'未打卡提醒', group='im-serve-attend', url='')

