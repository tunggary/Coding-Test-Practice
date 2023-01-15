import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

answer = []
nodes = deque([i for i in range(1,n+1)])

while True:
  if len(nodes) == 1:
    answer.append(nodes.popleft())
    break
  nodes.rotate(-(m-1))
  answer.append(nodes.popleft())
  
print('<', ', '.join(map(str, answer)), '>', sep='')