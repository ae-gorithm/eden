# 친구비
# 친구 관계를 연결된 그래프들로 만들자
# 각각 그룹에서 최소 비용들만 다 더하면 최소 친구비 알 수 있음
import sys
sys.setrecursionlimit(10**6)

def min_a(student, graph, visited):
  visited[student] = True
  result = A[student-1]

  for friend in graph[student]:
    if not visited[friend]:
      result = min(result, min_a(friend, graph, visited))

  return result

N, M, k = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N+1)

result = 0
for student in range(1, N+1):
  if not visited[student]:
    min_num = min_a(student, graph, visited)
    result += min_num

if k >= result:
  print(result)
else:
  print("Oh no")