# 输入0-10的整数，输出对应位数的自幂数信息

# 定义不同位数自幂数的名称
def get_armstrong_name(n):
    names = {
        0: "0位数",
        1: "独身数",
        2: "2位数自幂数",
        3: "水仙花数",
        4: "四叶玫瑰数",
        5: "五角星数",
        6: "六合数",
        7: "北斗七星数",
        8: "八仙数",
        9: "九九重阳数",
        10: "十全十美数"
    }
    return names.get(n, f"{n}位数自幂数")

# 判断一个数是否为自幂数
def is_armstrong_number(num, n):
    # 处理0的特殊情况
    if n == 0:
        return num == 0
    
    temp = num
    sum_of_powers = 0
    
    # 计算每个位上的数字的n次幂之和
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n
        temp //= 10
    
    return sum_of_powers == num

# 计算并显示指定位数的自幂数
def find_armstrong_numbers(n):
    name = get_armstrong_name(n)
    
    if n == 0:
        print(f"{name}：")
        print(f"数量：1")
        print(f"具体数值：[0]")
        return
    
    # 确定搜索范围
    start = 10 ** (n - 1)
    end = 10 ** n
    
    # 特殊处理1位数的情况
    if n == 1:
        start = 0
    
    # 收集自幂数
    armstrong_numbers = []
    for num in range(start, end):
        if is_armstrong_number(num, n):
            armstrong_numbers.append(num)
    
    # 输出结果
    print(f"{name}：")
    print(f"数量：{len(armstrong_numbers)}")
    print(f"具体数值：{armstrong_numbers}")

# 获取用户输入并执行程序
while True:
    try:
        n = int(input("请输入0-10之间的整数："))
        if 0 <= n <= 10:
            find_armstrong_numbers(n)
            break
        else:
            print("输入无效，请重新输入0-10之间的整数！")
    except ValueError:
        print("输入无效，请输入一个整数！")