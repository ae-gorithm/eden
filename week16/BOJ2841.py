# 외계인의 기타 연주
import sys
input = sys.stdin.readline

N, P = map(int, input().split())
result = 0

# 1~6번 줄 사용하므로 인덱스 0은 비워두기
stacks = [[] for _ in range(7)]

for _ in range(N):
    n, p = map(int, input().split())
    stack = stacks[n]

    while stack and stack[-1] > p:
        stack.pop()
        result += 1

    if stack and stack[-1] == p:
        continue

    stack.append(p)
    result += 1

print(result)
