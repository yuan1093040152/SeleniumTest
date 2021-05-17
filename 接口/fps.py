#coding=utf-8
#FPS测试，满分60，要避免动作不流畅的最低是30，要避免动作不流畅的最低是30
import os
import time
counter =10
#通过包名与activity名，获取帧数（查看之前记得滑动APP界面，以便获取数据）
content = os.popen("adb -s 5f95c93a shell dumpsys gfxinfo  com.jjshome.optionalexam")
#读取行数
data = content.readlines()
print (data)
start = 0
end = 0
i = 0
#为获得帧数据，先找具有代表性的开始行与结束行的字段“Draw"、"View hierarchy:"
for line in data:
    if "Draw" in line:
        start = i
        print ("start:",start)

    if "View hierarchy:" in line:
        end = i
        print ("end",end)
    i = i+1
#精确定位帧数据的开始行与结束行
result = data[start+1:end-1]
print (type(result))
print (result)
print ('--------------------------------------------------------------')
#未操作所测试的APP时，没有数据
if len(result) == 0:
    print ("没有数据，请操作app哈哈哈")

else:
    Exceed = 0      #超过16ms的帧数
    Lower = 0       #低于16ms的帧数
    addwait = 0       #额外等待的帧数
    addsum = 0
    for a in result:    
        #用""代替"\r\n"，去掉"\r\n"
        a = a.replace("\r\n","")
        print (a)
        datalist = a.split("\t")     #以"\t"对数据进行切片
        print ("list=",datalist)
        # addsum = addsum + float(datalist[4])   #计算FPS总和
        # print addsum
        #对每行帧数据进行加和操作
        sum = float(datalist[1]) + float(datalist[2]) + float(datalist[3]) + float(datalist[4])
        
        print ('sum    :',sum)

        addsum = addsum + float(sum)   #计算FPS总和
        print ('addsum    :',addsum)

        if (sum - 16) > 0:
            Exceed = Exceed + 1

            # 将float类型转化为整型，若sum=32，则addwait=1，若addwait=34，则addwait=2
            addwait = addwait + int(sum/16)
        else:
            Lower = Lower + 1

        # sum2 = sum1 + float(datalist[4])

    print ('fps总和为:%fms'%addsum)
    # print 'Number(>16ms)  :',Exceed
    print ('fps大于16ms的有:%d个'%Exceed)
    # print 'Number(<=16ms)  :',Lower
    print ('fps小于等于16ms的有:%d个'%Lower)
    fps = float(float(Exceed)/(float(Exceed) + float(Lower)))*100   #FPS大于>16ms 百分比
    avg = float(float(addsum)/(float(Exceed) + float(Lower)))    #FPS平均值
    # fps1 = str(fps) + '%'
    # print 'fps    :',fps,'%'
    print ('fps占比为：%f'%fps,'%')
    # print 'avg    :',avg,'ms'
    print ('fps平均值为：%fms'%avg)








        #     #计算公式：流畅的帧数/总共用的帧数(总的帧数+额外等待的帧数)=流畅度得分（满分60）
        # fpssorce = (len(result) - Exceed)*60/(len(result)+addwait)
        # print "fpsscore is %d" % int(fpssorce)
        # #好啦，完毕
