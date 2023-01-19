import sys
from collections import deque, defaultdict

t = int(sys.stdin.readline())
for _ in range(t):
  answer = 0
  n,m = map(int, sys.stdin.readline().split())
  count_dict = defaultdict(int)
  input_list = deque([(i, idx) for idx, i in enumerate(map(int, sys.stdin.readline().split()))])
  for input in input_list:
    count_dict[input[0]] += 1
  
  idx = 0
  for i in sorted(set(count_dict.keys()), reverse=True):
    while count_dict[i] > 0:
      priority, idx = input_list.popleft()
      if priority == i:
        answer += 1
        count_dict[i] -= 1
        if idx == m:
          print(answer)
          break
      else:
        input_list.append((priority, idx))