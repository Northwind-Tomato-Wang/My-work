import math
a=int(input('请输入三角形的直角边1(>0):'))
b=int(input('请输入三角形的直角边2(>0):'))
c=math.sqrt(a**2+b**2)
print(f'直角三角形的斜边为:{c:.2f}')