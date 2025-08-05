n="a1b2c3d4"
temp=""
res=""
for i in n:
    if i.isdigit():
        temp=i+temp
digit=0
for k in n:
    if k.isdigit():
        res+=temp[digit]
        digit+=1
    else:
        res+=k
print(res)
        
