a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
c=list(a.items())+list(b.items())
d=list(set(c))
result=[]
for i in range(len(d)):
    if d[i][1]>=3000:
        result.append(d[i])
print(result)