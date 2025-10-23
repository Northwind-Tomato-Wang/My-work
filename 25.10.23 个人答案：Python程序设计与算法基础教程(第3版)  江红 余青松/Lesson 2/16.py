# 输入一个三位自然数，用三种方法输出其百位数、十位数、个位数

# 获取输入
while True:
    num = input("请输入一个三位自然数：")
    if num.isdigit() and 100 <= int(num) <= 999:
        num = int(num)
        break
    else:
        print("输入无效，请重新输入一个三位自然数！")

# 方法一：循环求余法
def method1(n):
    temp = n
    digits = []
    for _ in range(3):
        digits.append(temp % 10)  # 获取当前位的数字
        temp = temp // 10         # 去掉已处理的位
    # 因为是从低位到高位存储的，所以需要反转
    hundreds, tens, units = digits[2], digits[1], digits[0]
    print(f"方法一（循环求余法）：")
    print(f"百位：{hundreds}, 十位：{tens}, 个位：{units}")

# 方法二：divmod()函数法
def method2(n):
    hundreds, remainder = divmod(n, 100)  # 获取百位和余数
    tens, units = divmod(remainder, 10)   # 获取十位和个位
    print(f"方法二（divmod()函数法）：")
    print(f"百位：{hundreds}, 十位：{tens}, 个位：{units}")

# 方法三：map()函数法
def method3(n):
    # 将数字转换为字符串，然后使用map()转换每个字符为整数
    digits = list(map(int, str(n)))
    hundreds, tens, units = digits[0], digits[1], digits[2]
    print(f"方法三（map()函数法）：")
    print(f"百位：{hundreds}, 十位：{tens}, 个位：{units}")

# 调用三种方法
method1(num)
print()  # 空行分隔
method2(num)
print()  # 空行分隔
method3(num)