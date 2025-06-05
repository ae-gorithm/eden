import sys
sys.setrecursionlimit(100000)

# 알고리즘 수업 - 깊이 우선 탐색 1
N, M, R = map(int, input().split())

E = {}
visited = {}
# 정점은 1 ~ N
for i in range(1, N+1):
  E[i] = []
  visited[i] = 0

for _ in range(M):
  u, v = map(int, input().split())
  E[u].append(v)
  E[v].append(u)

order = 1
def dfs(r):
  global order
  visited[r] = order
  order += 1
  E[r].sort()
  
  for x in E[r]:
    if visited[x] == 0:
      dfs(x)
  
dfs(R)

for i in range(1, N+1):
  print(visited[i])