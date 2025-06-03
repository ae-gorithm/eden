# 후위 표기식2
# 첫쨰 줄 - 첫째 줄에 피연산자의 개수
# 둘째 줄 - 후위 표기식

N = int(input())
postfix = list(input())
values = [int(input()) for _ in range(N)]

def transfer_num(ch):
  index = ord(ch) - ord('A')
  return values[index]
  

stack = []
for p in postfix:
  if p in ['-', '+', '*', '/']:
    a = stack.pop()
    b = stack.pop()
    if p == '-':
      c = b - a
    elif p == '+':
      c = b + a
    elif p == '*':
      c = b * a
    elif p == '/':
      c = b / a
    stack.append(c)
    
  else:
    stack.append(transfer_num(p))

print(f"{stack[0]:.2f}")