# def abc(t):
#        for i in range(len(t)):
#         if t[i] != t[len(t)-1-i]:
#          return False
#        return True
 
# word = input()
# print(word)
# if abc(word):
#    print("입력하신 단어는 회문(Palindrome)입니다.")
# else :
#    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")
a=input()
b=str(reversed(a))
print(type(b))
if a==b: print('O')