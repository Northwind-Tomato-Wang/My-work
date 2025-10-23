import math
x=float(input('请输入一个数:'))
if x>=0:
    print(f'方法一：x={x:.2f},y={(x**2-3*x)/(x+1)+2*math.pi+math.sin(x):.2f}')
if x<0:
    print(f'方法一：x={x:.2f},y={math.log(-5*x)+6*(abs(x)+math.e**4)**(1/2)-(x+1)**3:.2f}')

if x>=0:
    print(f'方法二：x={x:.2f},y={(x**2-3*x)/(x+1)+2*math.pi+math.sin(x):.2f}')
else:
    print(f'方法二：x={x:.2f},y={math.log(-5*x)+6*(abs(x)+math.e**4)**(1/2)-(x+1)**3:.2f}') 

print("方法二：" if (x>=0) else "方法一："+"x=%.2f,y=%.2f"%(x,(x**2-3*x)/(x+1)+2*math.pi+math.sin(x) if (x>=0) else math.log(-5*x)+6*(abs(x)+math.e**4)**(1/2)-(x+1)**3))
