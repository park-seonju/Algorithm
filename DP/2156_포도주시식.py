n=int(input())
podo=[int(input()) for _ in range(n)]
dp = [0]
dp.append(podo[0])
if(n > 1):
    dp.append(podo[0] + podo[1])

print('@@',dp)
print('@@',podo)
# 연속 3잔을 마시지 않아야 하므로
# 1 : 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
# 2 : 이번 포도주를 먹고 이전 포도주도 먹은 경우
# 3 : 이번 포도주를 먹지 않아야 하는 경우
# 위 세가지 경우를 고려하여 max

for i in range(3, n + 1):
    # podo는 0부터 시작하므로 i - 1로 해준다.
    case_1 = podo[i - 1] + dp[i - 2]
    case_2 = podo[i - 1] + podo[i - 2] + dp[i - 3]
    case_3 = dp[i - 1]
    max_value = max(case_1, case_2, case_3)
    
    dp.append(max_value)
    print(dp)
print(dp[n])