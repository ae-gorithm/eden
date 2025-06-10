# 나이트의 이동
# 매 칸마다 나이트가 이동할 수 있는 경우는 최대 8가지의 경우
# 8 가지의 경우중, 하나를 선택해서 이동했을 때, 
# 1. dfs -> 해당 칸에서 또 이동할 수 있는 경우들을 탐색 -> 무한 탐색 (비적절)
# 2. bfs -> 나머지 7가지의 경우들을 다시 탐색 (적절)
#


# 나이트가 이동할 수 있는 0 ~ l-1 사이의 위치 
def knight_move(r, c, l, moves):
  can_moves = [
    [r-1, c-2], 
    [r-2, c-1], 
    [r-1, c+2], 
    [r-2, c+1],
    [r+1, c-2], 
    [r+2, c-1], 
    [r+1, c+2], 
    [r+2, c+1]
  ]
  for m in can_moves:
    if (0 <= m[0] < l) and (0 <= m[1] < l):
      moves.append(m)
  return

def checking(curpoint, endpoint):
  if (curpoint[0] == endpoint[0]) and (curpoint[1] == endpoint[1]):
    return True

def bfs(l, points, end_point, count):
  moves = []
  for cur_point in points:
    knight_move(cur_point[0], cur_point[1], l, moves)

  for move in moves:
    if checking(move, end_point):
      return count
  
  # 이번 카운트에서는 없었음
  return bfs(l, moves, end_point, count+1)

T = int(input())

for test_case in range(T):
  I = int(input())
  cur_r, cur_c = map(int, input().split())
  end_r, end_c = map(int, input().split())
  result = 0
  if (cur_r == end_r) and (cur_c == end_c):
    result = 0
  else:
    result = bfs(I, [[cur_r, cur_c]], [end_r, end_c], 1)

  # 각 케이스별 결과 출력
  print(result)
