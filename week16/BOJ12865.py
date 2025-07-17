# 평범한 배낭
# 재귀 -> 시간 초과 
# dp 써야함
# 2차원 dp 너무 어렵워용 ㅠ

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
  w, v = items[i-1][0], items[i-1][1]

  for w_limit in range(1, K+1):
    if w_limit < w:
      dp[i][w_limit] = dp[i-1][w_limit]
    else:
      dp[i][w_limit] = max(dp[i-1][w_limit], dp[i][w_limit-w] + v)

print(dp[N][K])