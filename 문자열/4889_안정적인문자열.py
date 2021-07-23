import sys
input=sys.stdin.readline
tc=0
while True:
    s=input().rstrip();tc+=1;cnt=0
    if s.startswith('-'):break
    stack=[]
    for i in s:
        if i=='{':
            stack.append(i)
        else:
            if not stack:
                stack.append('{')
                cnt+=1
            else:
                stack.pop()
    cnt+=len(stack)//2
    print('{}. {}'.format(tc,cnt))
