from collections import deque

# 추월
# 차선 변경이 금지 되있다해서 여러 차선 있는줄 ..
# 차선이 2개 이상이면 차선 갯수에 따라 답이 달라질 수 있어서
# 차선은 1개이고 그냥 순서 변경만 보는 것 같다.

N = int(input())
in_car = [input() for _ in range(N)]
out_car = [input() for _ in range(N)]
over_car = set()

result = 0
i, o = 0, 0
while (o < N):
 if in_car[i] in over_car:
  i+=1
  continue

 elif in_car[i] == out_car[o]:
  i += 1
  o += 1
 
 elif in_car[i] != out_car[o]:
  over_car.add(out_car[o])
  result += 1
  o += 1

print(result)