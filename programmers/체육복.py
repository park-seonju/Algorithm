def solution(n, lost, reserve):
    dict1={}
    cnt=0
    for i in range(1,n+1):
        dict1[i]=1
    for i in reserve:
        dict1[i]+=1
    for i in lost:
        dict1[i]-=1
    for key,value in dict1.items():
        if value==0 and 1<key<n:
            if dict1[key-1]>1:
                dict1[key-1]-=1
                dict1[key]+=1
            elif dict1[key+1]>1:
                dict1[key+1]-=1
                dict1[key]+=1
        elif value==0 and 1==key:
            if dict1[key+1]>1:
                dict1[key+1]-=1
                dict1[key]+=1
        elif value==0 and n==key:
            if dict1[key-1]>1:
                dict1[key-1]-=1
                dict1[key]+=1
    answer=0
    for key in dict1.keys():
        if dict1[key]:
            answer+=1
    return answer
print(solution(5,[2, 4],[1,2,5]))