result=[]

for i in range(2,10):
    list1=[]
    for j in range(1,10):
        if not (i*j)%3 or not (i*j)%7:  # 시간낭비
            continue
        list1.append(i*j)
    result.append(list1)
print(result)