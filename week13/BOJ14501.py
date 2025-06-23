# 퇴사
# 각 날짜를 선택한 경우와 선택하지 않은 경우 -> 깊이 탐색

N = int(input())
maps = [[0,0]]
for i in range(N):
  t, p = map(int, input().split())
  maps.append([t, p])

total_p = []
def dfs(day, cur_t, cur_p):
  if day > N:
    total_p.append(cur_p)
    return

  # 선택하지 않는 경우
  dfs(day+1, cur_t, cur_p)

  # 선택하는 경우
  if (cur_t < day) and (day + maps[day][0]-1 <= N):
    cur_t = day + maps[day][0] - 1
    cur_p = cur_p + maps[day][1]
    dfs(day+1, cur_t, cur_p)

dfs(1, 0, 0)
print(max(total_p))