# 수들의 합 2

# N개의 수로 된 수열 A[1], A[2], …, A[N]
# i번째 수부터 j번째 수까지의 합 A[i] + ... + A[j]가 M이 되는 경우의 수

N, M = map(int, input().split())
nums = list(map(int, input().split()))

count, start, end, sum = 0, 0, 0, 0

while True:
  if end == N and sum < M:
    break

  if sum < M:
    sum += nums[end]
    end += 1
  elif sum > M:
    sum -= nums[start]
    start += 1
  else:
    count += 1
    sum -= nums[start]
    start += 1
  

print(count)