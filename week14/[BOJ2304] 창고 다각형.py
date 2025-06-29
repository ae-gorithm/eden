# 창고 다각형
# 창고 다각형 면적이 가장 작은 창고

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

data = sorted(data, key = lambda x:x[0])

result = 0
current_L = data[0][0]
for idx in range(len(data)):
  P = data[idx]

  if P[0] < current_L:
    continue

  if idx == len(data)-1 :
    result += data[idx][1]
    break

  # case1: 자기 자신보다 처음으로 큰 막대
  # case2: 자기 자신보다 큰 막대가 없다면 그 중 가장 큰 친구한테 가기
  next_L = 0
  next_H = 0
  is_ascent = False
  for j in range(idx+1, len(data)):
    if data[j][1] > next_H:
      next_L, next_H = data[j][0], data[j][1]
    
    if next_H > P[1]:
      is_ascent = True
      break
  
  current_L = next_L    
  # 지붕이 올라가는 경우 (case1)
  if is_ascent:
    result += (next_L - P[0]) * P[1]

  # 지붕이 내려가는 경우 (case2)
  else :
    result += P[1]
    result += (next_L - P[0] -1) * next_H  

print(result)