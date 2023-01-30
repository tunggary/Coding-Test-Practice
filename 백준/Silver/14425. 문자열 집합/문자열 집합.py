import sys

n,m = map(int, sys.stdin.readline().split())  
strings = set()
answer = 0

for _ in range(n):
  input = sys.stdin.readline().rstrip()
  strings.add(input)
  
for _ in range(m):
  input = sys.stdin.readline().rstrip()
  if input in strings:
    answer += 1
    
print(answer)