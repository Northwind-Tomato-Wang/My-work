for i in range(0,int(100/5+1)):
    for j in range(0,int((100-5*i)//3+1)):
        k=100-5*i-3*j
        if i+j+3*k==100:
            print(f"公鸡有{i}只，母鸡有{j}只，小鸡有{k}只")