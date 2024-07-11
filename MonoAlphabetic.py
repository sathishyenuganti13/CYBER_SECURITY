import random

key = input("enter key : ")
keys=[]

for i in key:
    keys.append(i)


msg = input("enter the msg to be transfered : ")

keys=list(set(keys))

if len(keys)!=26:
    for i in msg:
        if i not in keys and i.isalpha():
            keys.append(i)

dic = {}

def unique(l):
    res=[]
    for i in l:
        if i not in res and i.isalpha():
            res.append(i)
    return res

for k in unique(msg.lower()):
    if k.isalpha():
        a=random.randint(0,(len(keys)-1))
        dic.update({k:keys[a]})
        keys.pop(a)

print("dictionary : ",dic)

cipher = ""
for i in msg:
    if i.isalpha():
        if i.islower():
            cipher+=dic[i]
        else:
            cipher+=dic[i.lower()].upper()
    else:
        cipher+=i

print("cipher text : ",cipher)
