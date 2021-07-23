def solution(record):
    answer = []
    user={}
    change={}
    for i in record:
        info=i.split()
        if info[0]=='Enter':
            user[info[1]]=info[2]
        elif info[0]=='Change':
            change[info[1]]=info[2]

    for i in record:
        info=i.split()
        ans=""
        if info[0] == "Enter":
            if change.get(info[1]) is None:
                ans+=user[info[1]]+'님이 들어왔습니다.'
            else:
                ans+=change[info[1]]+'님이 들어왔습니다.'
        elif info[0]=="Leave":
            if change.get(info[1]) is None:
                ans+=user[info[1]]+'님이 나갔습니다.'
            else:
                ans+=change[info[1]]+'님이 나갔습니다.'
        elif info[0]=="Change":continue
        answer.append(ans)
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))