h=int(input("总头数："))
t=int(input("总腿数："))

# 解方程方法：设鸡为 x，兔为 y
# 方程组：x + y = h, 2x + 4y = t
# 由方程可得：y = (t - 2h)/2, x = h - y


# 先进行基本可解性判断
if t % 2 != 0 or not (2 * h <= t <= 4 * h):
    print("无解：腿数必须为偶数，且满足 2h ≤ t ≤ 4h")
else:
    # 代数（不依赖第三方库）的直接解
    y = (t - 2 * h) // 2
    x = h - y
    if x < 0 or y < 0:
        print("无解：解出负数")
    else:
        print("解方程方法求得：鸡有%d只，兔有%d只" % (x, y))
    
    for i in range(h + 1):
        if 2 * i + 4 * (h - i) == t:
            print("循环方法求得：鸡有%d只，兔有%d只" % (i, h - i))


# 保留原有：循环枚举的对照方法（用于验证）
if t % 2 == 0 and 2 * h <= t <= 4 * h:
    for i in range(h + 1):
        if 2 * i + 4 * (h - i) == t:
            print("循环方法求得：鸡有%d只，兔有%d只" % (i, h - i))
    