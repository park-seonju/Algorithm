# 효율성 실패풀이
# def solution(s):
#     L=len(s)
#     idx=0
#     while idx<L-1:
#         if s[idx] == s[idx+1]:
#             s=s[:idx]+s[idx+2:]
#             L-=2
#             if idx==0:idx=-1
#             else:idx-=2
#         idx+=1
#     if not s: return 1
#     else: return 0

def solution(s):
    stack=[]
    for i in s:
        if not stack: stack.append(i)
        else:
            if stack[-1]==i:stack.pop()
            else:stack.append(i)
        
    if not stack: return 1
    else: return 0
print(solution('abcdeffedcba'))