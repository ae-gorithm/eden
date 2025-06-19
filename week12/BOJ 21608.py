# 상어 초등학교
# 교실은 N×N 크기 
# 처음에는 무조건 (2, 2) 자리에 배치
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def seat(student, likes, room):
    N = len(room)
    candidates = []

    for x in range(N):
        for y in range(N):
            if room[x][y] != 0:
                continue
            like_cnt = 0
            empty_cnt = 0

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if room[nx][ny] in likes:
                        like_cnt += 1
                    elif room[nx][ny] == 0:
                        empty_cnt += 1

            candidates.append((-like_cnt, -empty_cnt, x, y))

    candidates.sort()
    _, _, fx, fy = candidates[0]
    room[fx][fy] = student
    return room

N = int(input())
room = [[0] * N for _ in range(N)]
likes_map = {}
# 좌석 배정
for i in range(N*N):
  nums = list(map(int, input().split()))

  key = nums[0]
  values = nums[1:]
  likes_map[key] = values
  seat(key, values, room)

# 만족도 계산
result = 0
for x in range(N):
  for y in range(N):
    student = room[x][y]

    likes = likes_map[student]
    cnt = 0
    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]
      if 0 <= nx < N and 0 <= ny < N:
          if room[nx][ny] in likes:
              cnt += 1

    # 점수 더하기 
    if cnt == 0:
       result += 0
    elif cnt == 1:
       result += 1
    elif cnt == 2:
       result += 10
    elif cnt == 3:
       result += 100
    elif cnt == 4:
       result += 1000
       
print(result)