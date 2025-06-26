# AC
# R은 배열에 있는 수의 순서를 뒤집는 함수이고, 
# D는 첫 번째 수를 버리는 함수
from collections import deque 

T = int(input())
result = []
for test_case in range(T):
  P = list(input())
  n = int(input())
  if n == 0:
    _ = input()
    X = deque()
  else:
    X = deque(map(int, input()[1:-1].split(",")))

  is_reverse = False
  is_error = False
  for p in P:
    # print(X)
    if p == 'R':
      is_reverse = not is_reverse

    elif p == 'D':
      if len(X) == 0:
        is_error = True
        break
      
      # 삭제
      if is_reverse:
        X.pop()
      else:
        X.popleft()

  # 출력
  if is_error:
    result.append("error")

  elif not is_reverse:
    result.append("[" + ",".join(map(str, X)) + "]")
  
  else:
    X.reverse()
    result.append("[" + ",".join(map(str, X)) + "]")

for r in result:
  print(r)