participant=["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
def solution(participant, completion):
    answer = ''
    temp=0
    dic={}
    for part in participant:
        dic[hash(part)]=part
        temp+=int(hash(part))
    for com in completion:
        temp-=hash(com)
    answer=dic[temp]
    return answer
print(solution(participant,completion))