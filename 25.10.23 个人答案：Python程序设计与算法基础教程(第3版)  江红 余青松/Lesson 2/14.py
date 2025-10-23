import random
import math
a=random.randint(0,100)
b=random.randint(0,100)
c=math.gcd(a,b)
d=a*b/c
print(f'两个随机数分别是{a}和{b}')
print(f'最大公约数是{c}，最小公倍数是{d}')
