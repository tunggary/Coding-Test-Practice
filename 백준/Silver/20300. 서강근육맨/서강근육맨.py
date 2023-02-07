import sys
from collections import deque

n = int(sys.stdin.readline().strip())
loss = list(map(int, sys.stdin.readline().strip().split()))
loss.sort()
loss_deq = deque(loss)
answer = 0
if len(loss) % 2 != 0:
  answer = loss_deq.pop()
  
while loss_deq:
  answer = max(answer, loss_deq.popleft() + loss_deq.pop())

print(answer)