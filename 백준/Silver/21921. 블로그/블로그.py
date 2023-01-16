import sys

n, x = map(int, sys.stdin.readline().split())
visited = list(map(int, sys.stdin.readline().split()))

sum_visitor = sum(visited[:x])
max_visitor = sum_visitor
i, j = 0, x - 1
count = 1

while j < n - 1:
    sum_visitor -= visited[i]
    i += 1
    j += 1
    sum_visitor += visited[j]
    if sum_visitor > max_visitor:
      max_visitor = sum_visitor
      count = 1
    elif sum_visitor == max_visitor:
      count += 1

print('SAD' if max_visitor == 0 else f'{max_visitor}\n{count}')