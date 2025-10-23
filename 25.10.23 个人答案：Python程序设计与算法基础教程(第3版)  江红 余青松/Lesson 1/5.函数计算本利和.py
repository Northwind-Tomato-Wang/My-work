def getValue(b,r,n):
    return b*(1+r/100)**n
b=float(input('请输入本金:'))
r=float(input('请输入年利率:'))
n=int(input('请输入年份:'))
interest=getValue(b,r,n)
print(f'本利和为:{interest:.2f}')