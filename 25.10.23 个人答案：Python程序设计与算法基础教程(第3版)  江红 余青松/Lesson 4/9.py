stud= [{'sid':'103','Chinese':90,'Math':95,'English': 92}, {'sid': '101','Chinese':80,'Math':85,'English':82},{'sid':'102','Chinese':70,'Math': 75,'English':72}]
dic={}
for i in stud:
    sid=i['sid']
    score=[i['Chinese'],i['Math'],i['English']]
    dic[sid]=score

for sid in sorted(dic.keys(), key=lambda x: int(x)):
    print(sid, dic[sid])