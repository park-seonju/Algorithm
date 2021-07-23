import sys
sys.setrecursionlimit(10**9)
 
N=int(sys.stdin.readline())
Tree=[[] for _ in range(N+1)]
check=[0 for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    Tree[u].append(v)
    Tree[v].append(u)
DP=[[0,0] for _ in range(N+1)]
 
check=[True for _ in range(N+1)]
def DFS(cur):
    check[cur]=False#방문체크
    DP[cur][0]=1#현재 노드 포함할때
    DP[cur][1]=0#현재 노드 포함하지 않을때
    for i in Tree[cur]:#연결된 노드 탐색
        if check[i]:#자식노드라면 
            DFS(i)
            DP[cur][0]+=DP[i][1]#현재노드 포함했을때
            DP[cur][1]+=max(DP[i][0],DP[i][1])#현재노드를 포함 안했을때
 
DFS(1)
print(N-max(DP[1][0],DP[1][1]))



import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline

def makeIt(parent, child, flag):

    if dp[child][flag] >= 0: return dp[child][flag]

    if flag:
        result = 1
        for i in link[child]:
            if i != parent:
                result += min(makeIt(child, i, 1), makeIt(child, i, 0))
        dp[child][flag] = result
        return result
    
    result = 0
    for i in link[child]:
        if i != parent:
            result += makeIt(child, i, 1)
    dp[child][flag] = result
    return result

n = int(input())
link = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

dp = [[-1]*2 for _ in range(n+1)]
link[0].append(1)
makeIt(0,0,1)
print(min(dp[1][0], dp[1][1]))