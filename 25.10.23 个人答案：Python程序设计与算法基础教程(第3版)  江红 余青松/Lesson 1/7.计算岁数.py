import datetime

name=input('请输入姓名:')
birth=int(input('请输入出生年份:'))
age=datetime.datetime.now().year-birth
print(f'您好！{name}。您{age}岁。')