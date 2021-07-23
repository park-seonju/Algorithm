x = int(input())
y=''
while x>0:
    y=str(x%2)+y  # str+ 바로옆에 붙히는 것 이므로
    x//=2
print(y)