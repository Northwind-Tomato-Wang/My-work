a = input()
if a == a[::-1]:
    print("方法一：是回文")
else:
    print("方法一：不是回文")

for i in range(len(a)//2):
    if a[i] != a[len(a)-1-i]:
        print("方法二：不是回文")
        break
else:
    print("方法二：是回文")

lst = []
for i in a:
    lst.append(i)
if lst == list(reversed(lst)):
    print("方法三：是回文")
else:
    print("方法三：不是回文")

if a == ''.join(reversed(a)):
    print("方法四：是回文")
else:
    print("方法四：不是回文")

# 方法五：递归判断
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

if is_palindrome(a):
    print("方法五：是回文")
else:
    print("方法五：不是回文")

