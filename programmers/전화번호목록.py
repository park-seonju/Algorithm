a=["123","12345","12",'67']
a.sort()
answer=True
for i in range(len(a)-1):
    if a[i] in a[i+1][:len(a[i])]:
        answer=False
        break