import math
a = 1
b = -10
c = 16

# 计算判别式
discriminant = b**2 - 4*a*c

# 根据判别式的值求解方程
if discriminant > 0:
    # 有两个不同的实根
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f'方程 {a}x² + {b}x + {c} = 0 有两个不同的实根:{x1:.1f}, {x2:.1f}')
elif discriminant == 0:
    # 有一个实根（重根）
    x = -b / (2*a)
    print(f'方程 {a}x² + {b}x + {c} = 0 有一个实根（重根）:{x:.1f}')
else:
    # 有两个共轭复根
    real_part = -b / (2*a)
    imag_part = math.sqrt(-discriminant) / (2*a)
    print(f'方程 {a}x² + {b}x + {c} = 0 有两个共轭复根:')
    print(f'x1 = {real_part:.1f} + {imag_part:.1f}i')
    print(f'x2 = {real_part:.1f} - {imag_part:.1f}i')