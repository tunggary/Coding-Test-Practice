import sys

n,m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
sum_board = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    sum_board[i][j] = sum_board[i-1][j] + sum_board[i][j-1] - sum_board[i-1][j-1] + board[i-1][j-1]
    
for x1,y1,x2,y2 in commands:
  print(sum_board[x2][y2] - sum_board[x1-1][y2] - sum_board[x2][y1-1] + sum_board[x1-1][y1-1])