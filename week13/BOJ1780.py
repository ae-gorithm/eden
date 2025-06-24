# 종이의 개수

# 종이가 다 같은 수로 되었는지 확인
def check_paper(paper):
  num = paper[0][0]
  for row in paper:
    for e in row:
      if e != num:
        return False
  return True

# 종이를 같은 크기의 종이 9개로 자르고 반환하기
def divide_paper(paper, new_papers):
  n = len(paper)
  block = len(paper) // 3
  
  for i in range(0, n, block):
    for j in range(0, n, block):
      new_papers.append([row[j:j+block] for row in paper[i:i+block]])
  return

# 입력 시작
N = int(input())
papers = []
paper = []

for i in range(N):
  rows = list(map(int, input().split()))
  paper.append(rows)
papers.append(paper)

minus_one = 0
zero = 0
one = 0
isBreak = False
while True:
  new_papers = []
  for p in papers:
    if check_paper(p):
      if p[0][0] == -1:
        minus_one += 1
      elif p[0][0] == 0:
        zero += 1
      else:
        one += 1
      
      if len(papers[0][0]) == 1:
        isBreak = True
    else:
      divide_paper(p, new_papers)
  
  if isBreak:
    break
  papers = new_papers

print(minus_one)
print(zero)
print(one)
      