n=input()
c_a=0
c_n=0
c_else=0
for i in n:
    if i.isdigit():
        c_n+=1
    elif i.isalpha():
        c_a+=1
    else:
        c_else+=1
print("Count of alpha:",c_a)
print("Count of numbers:",c_n)
print("Count of everything else:",c_else)
