total=0
temp=100
ans=0

for _ in range(10):
    num=int(input())
    total+=num
    if total==100:
        ans=total
        temp=0
    if temp>=abs(100-total):
        if temp==abs(100-total):
            ans=total
            continue
        temp=100-total
        ans=total
print(ans)