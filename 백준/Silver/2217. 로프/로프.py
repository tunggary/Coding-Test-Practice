import sys

n = int(sys.stdin.readline().strip())
rope = [int(sys.stdin.readline().strip()) for _ in range(n)]

rope.sort(reverse=True)
answer = 0

for i in range(n):
  answer = max(rope[i] * (i+1), answer)
    
print(answer)