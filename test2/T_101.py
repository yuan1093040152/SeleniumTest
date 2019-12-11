# coding=utf-8
# 韩信带1500名兵士打仗,战死四五百人,站3人一排,多出2人;站5人一排,多出4人;站7人一排,多出6人

def cc():
	for x in xrange(1000,1100):
		if x%3==2:
			if x%5==4:
				if x%7==6:
					# return x
					print (x)


# cc()
def aa():
	A = ['a','b','c']
	B = [1,2,3,]
	C = {'a1':20,'b2':30,'c3':40,'c4':50,'a3':60}
	# print (A[4])
	for i in range(len(A)):
		# print (A[i])
		value = C[A[i]+str(B[i])]
		print (value)

# aa()


# 20190710   不用sum，最多一个+号，一行代码（不包含导包）实现1到10的累加



# 20190711   一行代码，求1-100之间大于10且小于90的数字的平均值