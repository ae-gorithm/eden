# 종이의 개수
N = int(input())
paper = []
for i in range(N):
  rows = list(map(int, input().split()))
  paper.append(rows)

count = {-1: 0, 0: 0, 1: 0}

# 종이가 다 같은 수로 되었는지 확인
def check_paper(r_index, c_index, block):
  num = paper[r_index][c_index]
  isSame = True
  
  for r in range(r_index, r_index + block):
    for c in range(c_index, c_index + block):
      if paper[r][c] != num:
        isSame = False
        break
      if not isSame:
        break
  
  if isSame:
    count[num] += 1
  else:
    new_block = block // 3
    for n_r in range(0, block, new_block):
      for n_c in range(0, block, new_block):
        check_paper(r_index + n_r, c_index + n_c, new_block)
  

# 종이를 같은 크기의 종이 9개로 자르고 반환하기
# def divide_paper(paper, new_papers):
#   n = len(paper)
#   block = len(paper) // 3
  
#   for i in range(0, n, block):
#     for j in range(0, n, block):
#       new_papers.append([row[j:j+block] for row in paper[i:i+block]])
#   return

# 인덱싱을 저장하며 재귀적으로 호출
block = N
check_paper(0, 0, block)

print(count[-1])
print(count[0])
print(count[1])
      