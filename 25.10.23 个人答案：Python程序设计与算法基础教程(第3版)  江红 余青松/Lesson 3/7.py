import math
list=[]
list.append(float(input("请输入三角形边长a的值：")))
list.append(float(input("请输入三角形边长b的值：")))
list.append(float(input("请输入三角形边长c的值：")))
list.sort()
if list[0]+list[1]>list[2]:
    if list[0]**2+list[1]**2==list[2]**2:
        print("改三角形为直角三角形")
    elif list[0]==list[1] and list[1]==list[2]:
        print("该三角形为等边三角形")
    elif list[0]==list[1] or list[1]==list[2]:
        print("该三角形为等腰三角形")
else:
    print("不能构成三角形")
