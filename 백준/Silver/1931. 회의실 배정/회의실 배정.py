import sys

n = int(sys.stdin.readline().strip())
meetings = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

empty_time = 0
answer = 0

for start_time, end_time in meetings:
  if empty_time <= start_time:
    empty_time = end_time
    answer += 1
  
print(answer)
