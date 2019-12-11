#coding=utf-8

for b in range(1,10):
	aa = ''
	for x in range(1,b+1):
		c = x*b
		aa =aa+str(x)+'x'+str(b)+'='+str(c)+'   '
	print (aa)
		

# for i in range(1,10):
#     sumvalue = ''
#     for j in range(1,i+1):
#         sumvalue = str(i) + 'x' + str(j) + '=' '%2d'%i*j
#     print (sumvalue)



# for i in range(1,10):
# 	for j in range(1,10):
# 		result=i*j
# 		print'%d *%d = % -3d'%(i,j,result)
# 	print''

# for i in range(1,5):
# 	for j in range(1,5):
# 		for k in range(1,5):
# 			if( i != k ) and (i != j) and (j != k):
# 				print i,j,k