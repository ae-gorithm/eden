# 이분 그래프

K = int(input())
for test_case in range(K):
  V, E = map(int, input())

  graph = {i: [] for i in range(1, V+1)}
  
