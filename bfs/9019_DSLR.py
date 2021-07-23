# from collections import deque

# def D(command,num):
#     new_command = command +'D'
#     if num*2>9999:
#         if (num*2)%10000 in register:return
#         register.append((2*num)%10000)
#         q.append((new_command,(2*num)%10000))
#     else:
#         if 2*num in register:return
#         register.append(2*num)
#         q.append((new_command,2*num))

# def S(command,num):
#     new_command = command + 'S'
#     if num-1==0:
#         if 9999 in register:return
#         register.append(9999)
#         q.append((new_command,9999))
#         return
#     if (num-1) in register:return
#     register.append(num-1)
#     q.append((new_command,num-1))

# def L(command,num):
#     temp=str(num)
#     new_num=''
#     for i in range(1,len(temp)):
#         new_num+=temp[i]
#     new_num+=temp[0]
#     new_num=new_num.lstrip('0')
#     if not new_num:return
#     new_num=int(new_num)
#     if new_num in register:return
#     register.append(new_num)
#     q.append((command+'L',new_num))

# def R(command,num):
#     temp=str(num)
#     new_num=''
#     for i in range(len(temp)-1):
#         new_num+=temp[i]
#     new_num=temp[len(temp)-1]+new_num
#     new_num=new_num.lstrip('0')
#     if not new_num:return
#     new_num=int(new_num)
#     if new_num in register:return
#     register.append(new_num)
#     q.append((command+'R',new_num))

# for _ in range(int(input().rstrip())):
#     A,B=map(int,input().split())
#     q=deque()
#     q.append(('',A))
#     register=[]
#     while q:
#         command,num=q.popleft()
#         if num<0:continue
#         if num==B:
#             break
#         D(command,num)
#         S(command,num)
#         L(command,num)
#         R(command,num)
#     print(command)


from collections import deque

T = int(input())

for tc in range(1,T+1):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, ''))
    visited = [0]*10000
    visited[a] = 1
    answer = 0

    while q:
        now, step = q.popleft()
        if now == b:
            answer = step
            break
        first = (now*2) % 10000
        if visited[first] == 0:
            q.append((first, step+'D'))
            visited[first] = 1

        second = 9999 if now == 0 else now-1
        if visited[second] == 0:
            q.append((second, step+'S'))
            visited[second] = 1

        l = now//1000
        third = (now*10)%10000 + l
        if visited[third] == 0:
            q.append((third, step+'L'))
            visited[third] = 1

        m = (now%10) * 1000
        fourth = (now//10) + m
        if visited[fourth] == 0:
            q.append((fourth, step+'R'))
            visited[fourth] = 1
    print(answer)