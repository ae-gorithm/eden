# 222 풀링

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

def pooling(maps, N):
  row, col = N//2, N//2
  new_maps = [[0] * col for _ in range(row)]
  
  for r in range(row):
    for c in range(col):
      x = 2 * c
      y = 2 * r
      nums = [maps[y][x],maps[y+1][x],maps[y][x+1],maps[y+1][x+1]]
      
      sorted_nums = sorted(nums, reverse=True)
      new_maps[r][c] = sorted_nums[1]

  return new_maps

while True:
  if N == 1:
    break

  # 222-풀링
  maps = pooling(maps, N)
  N //= 2

print(maps[0][0])