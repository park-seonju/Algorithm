s=input()
t=input()
s_len=len(s)
t_len=len(t)
for i in range(s_len*t_len):
    if s[i%s_len] != t[i%t_len]:
        print(0)
        exit()
print(1)