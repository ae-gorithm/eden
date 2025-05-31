# 수들의 합 2

# N개의 수로 된 수열 A[1], A[2], …, A[N]
# i번째 수부터 j번째 수까지의 합 A[i] + ... + A[j]가 M이 되는 경우의 수

N, M = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(N):
  sum = nums[i]

  if sum == M:
    count += 1
    continue

  for j in range(i+1, N):
    sum += nums[j]
    if sum == M:
      count += 1
      break

print(count)