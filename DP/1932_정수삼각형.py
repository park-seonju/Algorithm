n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dp=[]
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            arr[i][0]=arr[i-1][0]+arr[i][0]
        elif i==j:
            arr[i][i]=arr[i-1][i-1]+arr[i][i]
        else:
            # 한단계 전 왼쪽 + 지금 vs 한단계 전 오른쪽 + 지금
            arr[i][j]=max(arr[i-1][j-1]+arr[i][j],arr[i-1][j]+arr[i][j])
print(max(arr[n-1]))



def make_it(row, col):
    if row == n:
        return 0

    if dp[row][col]: return dp[row][col]

    dp[row][col] = tree[row][col] + max(make_it(row+1, col), make_it(row+1, col+1))
    
    return dp[row][col]

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(i+1) for i in range(n)]
print(make_it(0, 0))