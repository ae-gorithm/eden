# 소수 사이 수열
# 양의 정수 k 
# 1. k가 소수인지 판단
# 2. k랑 가장 가까운 두 소수를 구하고 차이를 구하기 ?

def prime(k):
  for i in range(2, int(k**0.5)+1): 
    if k % i == 0:
      return False
  return True

T = int(input())
results = []
for test_case in range(T):
  k = int(input())
  
  # 1. k가 소수인지 판단
  if prime(k) == True:
    results.append(0)
    continue

  # 2. k랑 가장 가까운 두 소수를 구하고 차이를 구하기 ?
  # 작고 가까운 소수 구하기
  p1 = k-1
  p2 = k+1
  while True:
    if prime(p1) == True:
      break
    p1 -= 1

  while True:
    if prime(p2) == True:
      break
    p2 += 1

  results.append(p2-p1)
   
for result in results:
  print(result)