import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
  n,m = map(int, sys.stdin.readline().split())
  array = list(map(int, sys.stdin.readline().split()))
  docs = deque([(i, array[i]) for i in range(n)])
  max_value = max(array)
  answer = 0
  while len(docs) > 0:
    if docs[0][1] == max_value:
      answer += 1 
      if docs[0][0] == m:
        print(answer)
        break
      else:
        docs.popleft()
        max_value = max(docs, key=lambda x: x[1])[1]
    else:
      docs.rotate(-1)