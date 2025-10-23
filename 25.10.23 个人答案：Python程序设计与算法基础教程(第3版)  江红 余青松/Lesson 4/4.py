n=input()
n=n.split(" ")
new=[]
for i in n:
    if i not in new:
        new.append(i)
print(new)