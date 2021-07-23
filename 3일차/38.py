a=[input().split(' ')]
list1=[]
for i in range(len(a[0])-1,-1,-1):
    list1.append(a[0][i])
print(" ".join(list1))
