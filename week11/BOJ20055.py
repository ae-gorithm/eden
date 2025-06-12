# 컨베이어 벨트 위의 로봇
# 구현
from collections import deque 

N, K = map(int, input().split())
A = deque(map(int, input().split()))
robots = deque(False for _ in range(N))

step = 0
count = 0
while True:
  step += 1
  # 1. 벨트와 로봇 회전
  A.rotate(1)
  robots.rotate(1)
  robots[N-1] = False

  # 2. 로봇이 이동
  for i in range(N-2, -1, -1):
    r = robots[i]
    if r :
      if A[i+1] > 0 and not robots[i+1]:
        robots[i] = False
        robots[i+1] = True
        A[i+1] -= 1
        if A[i+1] == 0:
          count += 1
    
  # 2-1. 내리는 위치에 로봇이 있다면 즉시 내림
  robots[N-1] = False

  # 3. 올리는 위치에 로봇 올리기
  if A[0] > 0:
    robots[0] = True
    A[0] -= 1
    if A[0] == 0:
          count += 1

  # 4. 내구도 0인 칸의 갯수
  if count >= K:
     break

print(step)
