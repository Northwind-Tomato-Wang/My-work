def cross(a,b):
    ans=1
    a=a%10
    while b>0:
        ans *= a
        ans=ans%10
        b-=1
    return ans

t=int(input())
for i in range(t):
    arr = list(map(int, input().strip().split()))
    g=arr[6]%10
    if (cross(arr[0],arr[3])+cross(arr[1],arr[4])+cross(arr[2],arr[5]))%10==g:
        print("Yes")
    else:
        print("No")