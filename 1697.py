from collections import deque
n, k = tuple(map(int, input().split()))

m = max(n,k)*2
dp = [ m for _ in range(m+1)]

que = deque()
que.append((k,0))

while que :   #i 동생   n 언니
    print('que',que)
    i, count = que.popleft()
    print('dp',dp)
    if count >= dp[n] : continue
    
    if dp[i] > count : dp[i] = count
    else : continue

    if i == n : continue

    if i<n : que.append((n, count+n-i))
    else :
        que.append((i-1, count+1))
        
        if i%2==0 : que.append((i//2, count+1))
        else : que.append((i+1, count+1))   # +1 해주고 2를 나누는 것?

print(dp[n])