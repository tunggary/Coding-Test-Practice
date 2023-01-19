import sys

n = int(sys.stdin.readline())
expression = list(sys.stdin.readline().strip())
alphabet = { chr(ord('A')+i): float(sys.stdin.readline()) for i in range(n) }
stack = []

for char in expression:
  if char.isalpha():
    stack.append(alphabet[char])
  else:
    right = stack.pop()
    left = stack.pop()
    stack.append(eval(f'{left}{char}{right}'))
    
print(f'{stack[0]:.2f}')