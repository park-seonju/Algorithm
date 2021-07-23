a=input().split(', ')
row=int(a[0])
col=int(a[1])
result=[]
for i in range(row):
    list1=[] #0,1,2
    for j in range(col): #j 0,1,2,3,4
        list1.append(i*j)
    result.append(list1)
print(result)
