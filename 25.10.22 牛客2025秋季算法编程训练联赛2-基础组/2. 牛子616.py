n=int(input())
a=input()
dic={}
ans=0
for i in a:
    if int(i) in dic:
        dic[int(i)]+=1
    else:
        dic[int(i)]=1
print(dic)
if dic[6]>dic[1]:
    print(dic[1])
else:
    print(dic[6]-1)