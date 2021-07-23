import math
a=input().split(', ')
result=""
for r in a:
    result+='{:.2f}, '.format(2.*math.pi*float(r))
print(result[:-2])