import sys

t = int(sys.stdin.readline().strip())
dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
rotate_dir = [(1, 0), (0, -1), (0, -1), (-1,0), (-1, 0), (0, 1), (0, 1), (1, 0)]

def print_answer(n, new_board):
  for i in range(n):
    print(' '.join(map(str, new_board[i])))


def solve():
  n, d = map(int, sys.stdin.readline().strip().split())
  board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
  new_board = [[board[i][j] for j in range(n)] for i in range(n)]
  rotate_count = abs(d // 45)
  sign = 1 if d > 0 else -1
  for radius in range(1, n//2 + 1):
    for i in range(len(dir)):
      dx, dy = dir[i]
      x, y = n//2, n//2
      count = 0
      cur_index = i
      x += dx * radius
      y += dy * radius
      nx = x
      ny = y
      while count < rotate_count:
        rx, ry = rotate_dir[cur_index]
        if sign == -1:
          rx, ry = rotate_dir[(cur_index + len(rotate_dir) - 1) % len(rotate_dir)]
        nx, ny = nx + sign*radius*rx, ny + sign*radius*ry
        count += 1
        cur_index = (cur_index + sign) % len(rotate_dir)
      new_board[nx][ny] = board[x][y]
  print_answer(n, new_board)

for _ in range(t):
  solve()