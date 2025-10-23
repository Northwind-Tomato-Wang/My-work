import math

a=float(input('请输入a:'))
b=float(input('请输入b:'))
c=float(input('请输入c:'))

# 判断a和b的特殊情况
if a == 0:
    if b == 0:
        # a=b=0时无解
        print('该方程无解')
    else:
        # a=0但b≠0时只有一个解
        x = -c / b
        print(f'该方程是一元一次方程，有一个解：x={x:.2f}')
else:
    # 计算判别式
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # delta>0时有两个不等实根
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'该方程有两个不等实根：x1={x1:.2f}, x2={x2:.2f}')
    elif delta == 0:
        # delta=0时有两个相等实根
        x = -b / (2*a)
        print(f'该方程有两个相等实根：x={x:.2f}')
    else:
        # delta<0时有两个共轭复根
        real_part = -b / (2*a)
        imag_part = math.sqrt(-delta) / (2*a)
        print(f'该方程有两个共轭复根：x1={real_part:.2f}+{imag_part:.2f}i, x2={real_part:.2f}-{imag_part:.2f}i')
