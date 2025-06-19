# 대칭 차집합

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = a + b - 2 * len(A&B)
print(result)