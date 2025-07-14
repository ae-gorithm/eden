# 인간-컴퓨터 상호작용
# 사전에 저장하는 방식
# 누적합

S = list(input())
q = int(input())

# 알파벳 
# a ~ z 를 0 ~ 25로 매핑해서 사용하기
# idx = ord(a) - ord('a')  
prefix_sum = [[0] * (len(S)+1) for _ in range(26)]

for i in range(1, len(S)+1):
  s = S[i-1]
  for j in range(26):
    prefix_sum[j][i] = prefix_sum[j][i-1] 

  # 문자열 s의 누적합 증가
  idx = ord(s) - ord('a')
  prefix_sum[idx][i] += 1

results = []
for _ in range(q):
  a, l, r = input().split()
  l, r = int(l) + 1, int(r) + 1
  prefix = ord(a) - ord('a')
  count = prefix_sum[prefix][r] - prefix_sum[prefix][l-1]
  results.append(count)

for r in results:
  print(r)