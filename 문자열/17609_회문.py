import sys
input=sys.stdin.readline
t=int(input())

def palindrome(word,length):
    global flag
    for i in range(length//2):
            if word[i]!=word[length-1-i]:
                flag=True
                return i
    
for _ in range(t):
    s=input().rstrip()
    length=len(s)
    flag=False
    idx=palindrome(s,length)
    if flag:
        new1=s[:idx]+s[idx+1:]
        flag=False
        palindrome(new1,length-1)
        if flag:
            new2=s[:length-1-idx]+s[length-idx:]
            flag=False
            palindrome(new2,length-1)
            if flag:print(2);continue
        print(1);continue
    print(0)