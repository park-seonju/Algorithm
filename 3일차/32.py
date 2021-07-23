a=input()
alnum=0
digitnum=0
for i in a:
    if i.isalpha():
        alnum+=1
    elif i.isdigit():
        digitnum+=1
print("LETTERS",alnum)
print("DIGITS",digitnum)