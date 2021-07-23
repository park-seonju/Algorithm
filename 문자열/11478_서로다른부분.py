S=input()
length=len(S)
ans=set()
for i in range(1,length):
    for j in range(length-i+1):
        ans.add(S[j:j+i])
print(len(ans)+1)