# 안녕

N = int(input())
L = list(map(int, input().split())) # 잃는 체력
J = list(map(int, input().split())) # 얻는 기쁨

result = 0
def select(idx, sum, remain):
  global result
  if idx == N:
    result = max(result, sum)
    return

  # 선택 안하는 경우
  select(idx+1, sum, remain)

  # idx 선택하는 경우
  if remain - L[idx] > 0:
    remain -= L[idx]
    sum += J[idx]
    select(idx+1, sum, remain)

select(0, 0, 100)
print(result)