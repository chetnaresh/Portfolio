def num_reverse(n):
    temp=""
    number=n
    while n>0:
        num=n%10
        temp+=str(num)
        n=n//10
    res=number+int(temp)
    if res%2!=0:
        return True
    else:
        return False
print(num_reverse(36))