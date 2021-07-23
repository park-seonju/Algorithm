num=int(input())
result=[]
for i in range(1,num+1):
    if(num%i==0):
        result.append(i)
for i in result:
    print("{}(은)는 {}의 약수입니다.".format(i,num))
if(len(result)==2):
    print("{}(은)는 {}과 {}로만 나눌 수 있는 소수입니다.".format(num,result[0],result[1]))