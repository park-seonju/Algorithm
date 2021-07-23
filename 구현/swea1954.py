delta = (
    (0, 1),  # 열증가
    (1, 0),  # 행증가
    (0, -1),  # 열감소
    (-1, 0),  # 행감소
)
 
T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
 
    def snail():
        row = 0
        col = 0
        num = 1
        distance = max(N - 1,1)
        while True:
            for i in range(4):
                for _ in range(distance):
                    print(board)
                    board[row][col] = num
                    num += 1
                    if num > N ** 2:
                        return
                    dr, dc = delta[i]
                    row += dr
                    col += dc
            row += 1
            col += 1
            distance = max(1,distance-2)
 
    snail()
 
    print('#%d' % test_case)
    for r in range(N):
        for c in range(N):
            print(board[r][c], end=' ')
        print()