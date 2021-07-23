T=int(input())
for tc in range(T):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(2)]
    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]

    for j in range(2, n):
        arr[0][j] += max(arr[1][j - 1], arr[1][j - 2])
        arr[1][j] += max(arr[0][j - 1], arr[0][j - 2])

    ans = max(arr[0][n - 1], arr[1][n - 1])
    print(ans)