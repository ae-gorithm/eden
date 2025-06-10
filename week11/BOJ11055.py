# 가장 큰 증가하는 수열
# 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램
# dp 적용

N = int(input())
nums = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
  dp[i] = nums[i]
  for j in range(i):
    if nums[j] < nums[i]:
      dp[i] = max(dp[j]+nums[i], dp[i])


print(max(dp))