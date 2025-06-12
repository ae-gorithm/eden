# 강의실 배정

N = int(input())
rooms = []

for i in range(N):
  Si, Ti =  map(int, input().split())
  idx = -1
  
  for j in range(len(rooms)):
    room = rooms[j]
    is_possible = True
    for time in room:
      if Si < time[1] or Ti < time[0]:
        is_possible = False
    if is_possible:
      room.append([Si, Ti])
      idx = 0
      break

  # 없으면 새로운 룸 배정
  if idx == -1:
    rooms.append([[Si, Ti]])

print(len(rooms))