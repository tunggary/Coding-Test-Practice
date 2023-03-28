import sys

string = sys.stdin.readline().rstrip()

flag = False
current = ''
answer = ''
for char in string:
  if flag and char != '>':
    answer += char
    continue
  
  if char == '<':
    flag = True
    answer += (current[::-1] + char)
    current = ''
  elif char == '>':
    flag = False
    answer += char
  elif char == ' ':
    answer += (current[::-1] + char)
    current = ''
  else:
    current += char
    
print(answer + current[::-1])
