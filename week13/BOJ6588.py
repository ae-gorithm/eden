# 골드바흐의 추측

# 입력이 n (6 ≤ n ≤ 1000000)
# 출력은 
# "n = a + b" or "Goldbach's conjecture is wrong."

# 에라토스테네스의 체를 사용해서 소수를 한번에 구해두고
# 각 케이스에 대해서 가능한 지 탐색하자

def check_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

# 에라토스테네스의 체란?
# 특정 숫자 a가 소수인 경우 -> a의 배수는 소수가 될 수 없음을 이용하여
# 체로 거르듯이 범위 내의 모든 소수를 구하는 방법 
# O(NloglogN) 의 시간 복잡도를 가진다는데, 거의 선형으로 동작할 정도로 빠름
max = 1000000
is_prime = [True] * (max + 1)
is_prime[0] = False
is_prime[1] = False

for num in range(2, int(max ** 0.5) + 1):
  # 소수라면 자기 자신의 배수들은 모두 소수가 아님
  if is_prime[num]:
    for i in range(num * num, (max + 1), num):
      is_prime[i] = False

results = []
while True:
  n = int(input())
  if n == 0 :
    break

  # a는 최소 3부터 시작 3, 5, ... (최대)n/2
  is_wrong = True
  for a in range(3, n//2+1, 2):
    if is_prime[a] and is_prime[n-a]:
      results.append([n, a, n-a])
      is_wrong = False
      break
  
  if is_wrong:
    results.append(["Goldbach's conjecture is wrong."])
    
for r in results:
  if len(r) == 1:
    print(r[0])
  else:
    print(f"{r[0]} = {r[1]} + {r[2]}")

