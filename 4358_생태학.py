import sys
input = sys.stdin.readline
D = {}
total = 0
while 1:
    tree = input().rstrip()
    if not tree:
        break
    D[tree] = D.get(tree,0) + 1
    total +=1

D = sorted(D.items())

for i in D:
    print('%s %.4f' %(i[0],i[1]*100/total))