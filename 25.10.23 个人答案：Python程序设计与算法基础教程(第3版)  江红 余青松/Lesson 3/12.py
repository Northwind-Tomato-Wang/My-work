# 第一次下落：100 米；第一次反弹高度：50 米
height = 50
i = 1
dis = 100

# 到第10次落地，需要再经历 9 次“上+下”
while i <= 9:
    dis = dis + 2 * height
    height = height / 2
    i = i + 1

print("第10次落地时的总路程为：", round(dis, 6), "米")
print("第10次反弹的高度为：", round(height, 3), "米")