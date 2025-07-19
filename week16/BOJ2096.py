# 내려가기
import sys
input = sys.stdin.readline

N = int(input())
prev_max = [0] * 3
prev_min = [0] * 3

a, b, c = map(int, input().split())
prev_max = [a, b, c]
prev_min = [a, b, c]

for _ in range(N-1):
  a, b, c = map(int, input().split())

  cur_max = [0] * 3
  cur_min = [0] * 3

  cur_max[0] = max(prev_max[0], prev_max[1]) + a
  cur_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + b
  cur_max[2] = max(prev_max[1], prev_max[2]) + c

  cur_min[0] = min(prev_min[0], prev_min[1]) + a
  cur_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + b
  cur_min[2] = min(prev_min[1], prev_min[2]) + c

  prev_max = cur_max
  prev_min = cur_min

print(max(prev_max), min(prev_min))