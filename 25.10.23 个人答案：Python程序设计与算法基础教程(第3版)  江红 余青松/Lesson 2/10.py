import math
a=int(input('请输入三角形的边A:'))
b=int(input('请输入三角形的边B:'))
c=int(input('请输入三角形的边C:'))
if a+b>c and a+c>b and b+c>a:
    print("三角形的三条边为:",a,b,c)
    print("三角形的周长为:",a+b+c,"三角形的面积为:",round(math.sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))/4,1))
else:
    print('无法构成三角形！')
