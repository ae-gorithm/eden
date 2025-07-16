# 평범한 배낭

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
result = 0

def select(idx, cur_w, cur_v):
  global N
  if idx == N:
    global result
    result = max(result, cur_v)
    return

  w, v = items[idx][0], items[idx][1]

  if cur_w + w <= K:
    select(idx+1, cur_w + w, cur_v + v)
  
  select(idx+1, cur_w, cur_v)

select(0, 0, 0)

print(result)