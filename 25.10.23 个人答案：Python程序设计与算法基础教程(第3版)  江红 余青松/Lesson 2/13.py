while True:
    a=int(input("请输入非负整数n="))
    ji=1
    j=1
    ji2=1
    if a>=0:
        for i in range(1,a+1):
            ji *= i
        print("for循环：5!=",ji)
        while j<=a:
            ji2 *= j
            j += 1
        print("while循环：5!=",ji2)
        break
