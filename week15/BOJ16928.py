# 뱀과 사다리 게임

N, M = map(int, input().split())

up = sorted([list(map(int, input().split())) for _ in range(N)])
down = sorted([list(map(int, input().split())) for _ in range(M)])
check = [1] * 101
check[0] = -1

for u in up:
  check[u[0]] = u[1]

for d in down:
  check[d[0]] = 0


# 다음 칸을 선택할때 가능한 선택지 (1 ~ 6 중)
# 1. 제일 많이 전진하는 칸(뱀과 사다리가 없는)
# 2. 사다리를 가는 것(있다면)
min_count = 100
def forward(idx, count):
  global min_count
  if count > min_count:
    return

  if idx == 100:
    min_count = min(min_count, count)
    return

  next = idx
  for i in range(1, 7):
    new_idx = idx + i
    if new_idx>100:
      break

    if check[new_idx] == 0:
      continue

    if check[new_idx] == 1:
      next = new_idx
    
    if check[new_idx] >= 1:
      forward(check[new_idx], count+1)
  
  forward(next, count +1)

forward(1, 0)    
print(min_count)
    





