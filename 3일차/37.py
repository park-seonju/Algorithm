a=input()
num=0
for i in range(len(a)):
    if a[i]==a[len(a)-(i+1)]:
        num+=1
print(a)
if num==(len(a)):
    print('입력하신 단어는 회문(Palindrome)입니다.')
else :
    print('아닙니다.')

#if a==a[::-1]