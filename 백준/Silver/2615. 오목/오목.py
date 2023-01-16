import sys

N = 19
K = 4

board = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
color = 0
dir_list = [(-1,1),(0,1),(1,1),(1,0)]


for x in range(N):
  for y in range(N):
    if board[x][y] > 0:
      for dir in dir_list:
        nx = x + dir[0]
        ny = y + dir[1]
        count = 1
        if 0<=x-dir[0]<N and 0<=y-dir[1]<N and board[x][y] == board[x-dir[0]][y-dir[1]]:
          continue
        while 0<=nx<N and 0<=ny<N and board[nx][ny] == board[x][y]:
          count += 1
          if count == 5:
            if 0<=nx+dir[0]<N and 0<=ny+dir[1]<N and board[nx+dir[0]][ny+dir[1]] == board[x][y]:
              break
            print(board[x][y])
            print(x+1, y+1)
            sys.exit()
          nx += dir[0]
          ny += dir[1]
            
print(0)
      