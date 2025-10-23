x=float(input("请输入x："))
n=1
set=1
solution=1
while True:
    set=x**n
    for i in range(1,n+1):
        set=set/i
    solution+=set
    if set<1e-6:
        print("e的x次方的近似值为：",round(solution,6))
        break
    n=n+1