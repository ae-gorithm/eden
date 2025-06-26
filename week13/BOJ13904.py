# 과제

N = int(input())

works = {}
max_day = 0
for i in range(N):
  d, w = map(int, input().split())
  max_day = max(max_day, d)
  
  if d in works:
    works[d].append(w)
  else:
    works[d] = [w]

total_count = 0
for day in range(max_day, 0, -1):
  m_d, m_w = -1, -1

  # 기간 내 제일 큰 과제 점수의 과제 찾기
  for d in range(day, max_day+1):
    ws = works.get(d)
    if ws:
      w = max(ws)
      if w > m_w:
        m_d, m_w = d, w

  # 선정된 과제
  if m_d != -1:
    total_count += m_w
    works[m_d].remove(m_w)

print(total_count)