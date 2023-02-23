import sys

n,m,r = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for _ in range(r):
  # 회전
  for i in range(min(n,m)//2):
    row, col = i, i
    temp = board[row][col]
    
    for j in range(i+1, n-i):
      row = j
      prev = board[row][col]
      board[row][col] = temp
      temp = prev
    
    for j in range(i+1, m-i):
      col = j
      prev = board[row][col]
      board[row][col] = temp
      temp = prev
      
    for j in range(i+1, n-i):
      row = n - j - 1
      prev = board[row][col]
      board[row][col] = temp
      temp = prev
    
    for j in range(i+1, m-i):
      col = m - j - 1
      prev = board[row][col]
      board[row][col] = temp
      temp = prev
 

for i in range(n):
  print(' '.join(map(str, board[i])))
    
  