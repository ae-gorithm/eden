# 도영이가 만든 맛있는 음식
import itertools

N = int(input())
index, flavors = [], []
for i in range(N):
  index.append(i)
  flavors.append(list(map(int, input().split())))

result = 1000000000
# 적어도 한개 이상 선택해야 하므로
for count in range(1, N+1):
  print
  for idx in itertools.combinations(index, count):
    S, B = flavors[idx[0]][0], flavors[idx[0]][1]
    for i in range(1, count):
      S *= flavors[idx[i]][0]
      B += flavors[idx[i]][1]
    
    # 현재 재료로 만든 요리의 차이
    result = min(result, abs(S-B))

print(result)