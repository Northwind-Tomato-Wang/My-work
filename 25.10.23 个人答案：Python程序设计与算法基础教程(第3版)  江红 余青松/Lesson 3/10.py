import math
a=float(input("请输入a："))
sol=a/2
while abs(sol-math.sqrt(a))>1e-6:
    sol=(sol+a/sol)/2
print("平方根的近似值为：",round(sol,3))
