def second_highest(arr):
    temp=[]
    for i in arr:
        if i not in temp:
            temp.append(i)
    high=float('-inf')
    second=float('-inf')
    for j in temp:
        if j>high:
            second=high
            high=j
        elif j>second and j!=high:
            second=j
    if second==float('-inf'):
        return None
print(second_highest(arr=[1,7,89,4,3,45]))