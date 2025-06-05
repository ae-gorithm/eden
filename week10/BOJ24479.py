import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

E = {i: [] for i in range(1, N + 1)}
visited = {i: 0 for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(1, N + 1):
    E[i].sort(reverse=True)  

order = 1
stack = [R]

while stack:
    node = stack.pop()
    if visited[node] == 0:
        visited[node] = order
        order += 1
        for neighbor in E[node]:
            if visited[neighbor] == 0:
                stack.append(neighbor)

for i in range(1, N + 1):
    print(visited[i])
