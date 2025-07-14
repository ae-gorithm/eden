# 인간-컴퓨터 상호작용
# 사전에 저장하는 방식
# { a : [l, r, count] }

S = list(input())
q = int(input())
dict = {}
results = []

for i in range(q):
  a, l, r = input().split()
  l = int(l)
  r = int(r)
  
  if a in dict:
    p_l, p_r, count = dict[a][0], dict[a][1], dict[a][2]

    # 그냥 계산이 나은 경우 - 이전이랑 아예 안겹칠 때
    if p_r <= l :
      # l, r 사이의 알파벳 count
      count = 0
      for i in range(l, r+1):
        if S[i] == a :
          count += 1
      
      dict[a] = [l, r, count]
      results.append(count)
    
    else:
      while (p_l != l):
        if p_l < l :
          if S[p_l] == a:
            count -= 1
          p_l += 1
        
        elif p_l > l:
          if S[p_l-1] == a:
            count += 1
          p_l -=1
      
      while (p_r != r):
        if p_r < r:
          if S[p_r+1] == a:
            count += 1  
          p_r +=1
        
        elif p_r > r:
          if S[p_r] == a:
            count -= 1
          p_r -= 1
        
      dict[a] = [l, r, count]
      results.append(count)
  else:
    # l, r 사이의 알파벳 count
    count = 0
    for i in range(l, r+1):
      if S[i] == a :
        count += 1
    
    dict[a] = [l, r, count]
    results.append(count)

for r in results:
  print(r)