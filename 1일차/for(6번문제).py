student=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a=0
b=0
ab=0
o=0
for i in student:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='O':
        o+=1
    else:
        ab+=1
print("'A':{},'O':{},'B':{},'AB':{}".format(a,o,b,ab))