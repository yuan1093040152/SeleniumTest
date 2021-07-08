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

    # ##############################################
    # 从dubbo后台获取直连ip
    def dubboGetip(self, interface, huanjing, tanchuangbz):
        '''
        # 从dobbo中心获取服务的直连ip。
        :param interface: 服务名称
        :param huanjing: 调用环境
        :param tanchuangbz: 当获取不到ip时是否弹窗确认打开dubbo后台管理中心
        :return:
        '''
        # 弹窗确认结果，默认为False
        ry = False
        if u'正式' in huanjing or u'生产' in huanjing:
            huanjing = '172.16.4.223:8084'
        elif u'3.100' in huanjing or u'线下测试' in huanjing:
            huanjing = '172.16.4.114:9080'
        elif u'22.100' in huanjing or u'容器' in huanjing:
            huanjing = '172.16.22.100:9080'
        elif u'2.54' in huanjing or u'线上测试' in huanjing:
            huanjing = '192.168.3.70:9080'
        else:
            print (u'环境指定错误，默认使用3.100')
            huanjing = '172.16.4.114:9080'
        try:
            headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate",
                       "Connection": "keep-alive",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                       "Host": "172.16.4.223:8084",
                       "Cookie": "_ga=GA1.1.1890888338.1580476038; HISTORY=\"com.jjshome.im.service.dubbo.NimAccidService..../governance/services/com.jjshome.im.service.dubbo.NimAccidService/providers\\.\\.\\.\\.\\.\\.com.jjshome.im.service.dubbo.INimRoomService..../governance/services/com.jjshome.im.service.dubbo.INimRoomService/providers\"",
                       "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                       "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="}
            url = 'http://%s/governance/services/%s/providers' % (huanjing, interface)
            url_t = 'http://%s/governance/services?keyword=%s' % (huanjing, interface)
            # 发送请求，查询dubbo后台，获取ip和端口
            try:
                r = requests.get(url=url, headers=headers, timeout=5)
                r = re.findall('\d+\.\d+\.\d+\.\d+\:\d+', r.text)
            except:
                if tanchuangbz:
                    print("请求失败")
            # 如果获取ip和端口成功
            if r:
                print (r)
                print (re.split(':', r[0]))
                # 如果是容器则特殊处理
                if u'22.100' in huanjing or u'容器' in huanjing:
                    return ('172.16.22.100', '2008')
                return re.split(':', r[0])

        except:
            print ("获取不到IP和端口")



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
        # host = '192.168.196.6'   不知道什么原因这个IP会变，故不能写死
        # host = '192.168.214.26'
        # port = '26889'

        param = u'{"fromAccid":"servenumber000011","group":"%s","toAccids":[%s],"body":"{\\"type\\":8,\\"data\\":{\\"title\\":\\"%s\\",\\"content\\":\\"%s\\",\\"source\\":\\"im-serve-attend\\",\\"sourceName\\":\\"%s的温馨提示\\",\\"sourceType\\":\\"im-serve-fwsq\\",\\"url\\":\\"%s\\",\\"isOuterOpen\\":true}}"}' % (
            group, idsstr, moban, msg, moban, url)

        """
        {"fromAccid":"servenumber000011","group":"im-serve-attend","toAccids":["252613"],"body":"{\"type\":8,\"data\":{\"title\":\"今日未打卡提醒\",\"content\":\"今天未打卡名单：袁猛\",\"source\":\"im-serve-attend\",\"sourceName\":\"今日未打卡提醒的温馨提示\",\"sourceType\":\"im-serve-fwsq\",\"url\":\"\",\"isOuterOpen\":true}}"}

        """

        print(param)

        # param = {"fromAccid": 'servenumber000011', "toAccids": '["252613"]', "group": 'im-serve-attend',"body": '{"type":"8","data":"{"sourceName":"456","title":"567","content":"678","isOuterOpen":"true","sourceType":"im-serve-fwsq","source":"im-serve-attend","url":""}"}'}

        host,port = self.dubboGetip(interface=interface, huanjing=u'生产', tanchuangbz=False)

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

