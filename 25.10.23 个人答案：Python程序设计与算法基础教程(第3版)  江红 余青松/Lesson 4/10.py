import random

# 随机生成10个0~40的整数，允许重复
a = [random.randint(0, 40) for _ in range(10)]
b = [random.randint(0, 40) for _ in range(10)]

# 转为集合
set_a = set(a)
set_b = set(b)

print("集合a内容：", set_a)
print("集合b内容：", set_b)
print("集合a长度：", len(set_a))
print("集合b长度：", len(set_b))
print("集合a最大值：", max(set_a))
print("集合a最小值：", min(set_a))
print("集合b最大值：", max(set_b))
print("集合b最小值：", min(set_b))
print("a和b的交集：", set_a & set_b)
print("a和b的并集：", set_a | set_b)
print("a和b的差集（a-b）：", set_a - set_b)