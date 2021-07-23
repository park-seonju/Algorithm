result=[]
for i in range(100,301):
    a=int(i/100) # int로 해야함
    b=int(i/10)

    if(a % 2 == 0 and b % 2 == 0 and i % 2 == 0):
        result.append(str(i))
print(",".join(result))
