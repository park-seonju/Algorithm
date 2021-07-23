def bt(idx,n):
    if n==6:
        for i in range(K):
            if visited[i]:
                print(S[i],end=" ")
        print()
        return
        
    for i in range(idx,K):
        visited[i]=1
        bt(i+1,n+1)
        visited[i]=0
while True:
    arr=list((map(int,input().split())))
    if arr[0]==0:
        break
    K=arr[0]
    S=arr[1:]
    visited=[0 for _ in range(K)]
    bt(0,0)
    print()

# def lotto(x, cnt):
#     if cnt == 6:
#         for i in range(k):
#             if select[i]:
#                 print(a[i], end=' ')
#         print()
#         return

#     for i in range(x, k):
#         select[i] = 1
#         lotto(i+1, cnt+1)
#         select[i] = 0

# while True:
#     a = list((map(int, input().split())))
#     k = a[0]
#     if k == 0:
#         break
#     a = a[1:]
#     select = [0 for _ in range(k)]
#     lotto(0, 0)
#     print()