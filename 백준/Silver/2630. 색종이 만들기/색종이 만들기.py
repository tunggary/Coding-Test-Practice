import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [0, 0]

def divide_conquer(x, y, n):
  global answer
  color = graph[x][y]
  divide = False
  for i in range(x, x+n):
    for j in range(y, y+n):
      if graph[i][j] != color:
        divide = True
        break 
  if divide:
    divide_conquer(x, y, n//2)
    divide_conquer(x, y+n//2, n//2)
    divide_conquer(x+n//2, y, n//2)
    divide_conquer(x+n//2, y+n//2, n//2)
  else:
    answer[color] += 1

    
divide_conquer(0, 0, n)
print(f'{answer[0]}\n{answer[1]}')