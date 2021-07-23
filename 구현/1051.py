N,M=map(int,input().split())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().rstrip())))

if N>=M:
    bound=M
else:
    bound=N

ans = 0
for i in range(N):
    for j in range(M):
        for k in range(1,bound):
            if i+k<=N-1 and j+k<=M-1:
                if matrix[i][j]==matrix[i][j+k] and matrix[i][j]==matrix[i+k][j] and matrix[i][j] == matrix[i+k][j+k] :
                    if ans<k:
                        ans=k
print((ans+1)**2)