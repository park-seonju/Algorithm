import sys
#sys.stdin.readline() = input()
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

matrix=[[0]*(N+1) for i in range(N+1)] 

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    matrix[a][b]=matrix[b][a]=1

visit_list=[0]*(N+1)

num=-1

def dfs(V):
    global num #지양
    visit_list[V]=1 #방문한 점 1로 표시
    num+=1
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

print(num)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    global num
    while queue: #디큐로 해보기
        V=queue.pop(0)  
        for i in range(1, N+1):
            if(visit_list[i]==0 and matrix[V][i]==1):
                num+=1
                queue.append(i)
                visit_list[i]=1

print(num)
