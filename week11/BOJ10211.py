# Maximum Subarray
# DP 

T = int(input())
results = []

for test_case in range(T):
  N = int(input())
  X = list(map(int, input().split()))

  current_sum = max_sum = X[0]
  for i in range(1, N):
      current_sum = max(X[i], current_sum + X[i])
      max_sum = max(max_sum, current_sum)

  results.append(max_sum)

for result in results:
    print(result)
