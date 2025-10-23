n=int(input('请输入一个整数:'))
total=0
for i in range(1,n+1,2):
    if i%4 == 1:
        total += i
    else:
        total -= i
print(total)