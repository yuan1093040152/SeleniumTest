#coding=utf-8
import turtle
import datetime,time
 
def love():
    def func(x, y):
        main()
    turtle.title('2019年2月14日')
    lv=turtle.Turtle()
    lv.hideturtle()
    lv.getscreen().bgcolor('light blue')
    lv.color('yellow','red')
    lv.pensize(3)
    lv.speed(1)
    lv.up()
    lv.goto(0,-150)
    #开始画爱心
    lv.down()
    lv.begin_fill()
    lv.goto(0, -150)
    lv.goto(-175.12, -8.59)
    lv.left(140)

    pos = []
    for i in range(19):
        lv.right(10)
        lv.forward(20)
        pos.append((-lv.pos()[0], lv.pos()[1]))
    for item in pos[::-1]:
        lv.goto(item)
    lv.goto(175.12, -8.59)
    lv.goto(0, -150)
    lv.left(50)
    lv.end_fill()
    #写字
    lv.up()
    lv.goto(0, 80)
    lv.down()
    lv.write("祝大家：",font=(u"方正舒体",36,"normal"),align="center")
    lv.up()
    lv.goto(0, 0)
    lv.down()
    lv.write("情人节快乐！",font=(u"方正舒体",48,"normal"),align="center")
    lv.up()
    lv.goto(100, -210)
    lv.down()
    lv.write("",font=(u"华文琥珀",26,"bold"),align="right")
    lv.up()
    lv.goto(160, -190)
    time.sleep(5)
    # lv.resizemode('user')
    # lv.shapesize(4, 4, 10)#调整小乌龟大小，以便覆盖“点我”文字
    # lv.color('red', 'red')
    # lv.onclick(func)
    # lv.showturtle()
 
 
def main():
    pass
 
if __name__ == '__main__':
    if datetime.date.today() == datetime.date(2019, 02, 14): #YYYY年,MM月,DD日
        love()
    else:
        main()