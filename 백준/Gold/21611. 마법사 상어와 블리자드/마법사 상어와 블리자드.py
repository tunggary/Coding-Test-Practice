import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
magic = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
move = {
  1: (-1, 0),
  2: (1, 0),
  3: (0, -1),
  4: (0, 1)
}
rotate_pos_order = []
blown_ball = []

def get_rotate_pos_order():
  dir_order = [3, 2, 4, 1]
  x, y = n//2, n//2
  current_dir_index = 0
  current_move_distance = 1
  
  while True:
    for _ in range(2):
      dx, dy = move[dir_order[current_dir_index]]
      for _ in range(current_move_distance):
        x += dx
        y += dy
        if x < 0 or x >= n or y < 0 or y >= n:
          return
        rotate_pos_order.append((x, y))
      current_dir_index = (current_dir_index + 1) % 4
    current_move_distance += 1
  
def use_magic(dir, distance):
  dx, dy = move[dir]
  x, y = n//2, n//2
  for _ in range(1, distance + 1):
    x = x + dx
    y = y + dy
    if x < 0 or x >= n or y < 0 or y >= n:
      continue
    if board[x][y] == 0:
      continue
    board[x][y] = 0
    
def move_balls():
  # 다음 빈칸 위치
  next_empty_pos = deque([])
  for x, y in rotate_pos_order:    
    if board[x][y] == 0:
      next_empty_pos.append((x, y))
      continue
    if len(next_empty_pos) != 0:
      next_x, next_y = next_empty_pos.popleft()
      board[next_x][next_y] = board[x][y]
      board[x][y] = 0
      next_empty_pos.append((x, y))
      
def blowup_ball():
  prev = -1
  count = 1
  total_count = 0
  blown_ball_pos = []
  
  for x, y in rotate_pos_order:
    if board[x][y] == prev:
      count += 1
      blown_ball_pos.append((x, y))
    else:
      if count >= 4:
        total_count += 1
        blown_ball.append((board[blown_ball_pos[-1][0]][blown_ball_pos[-1][1]], count))
        for i, j in blown_ball_pos:
          board[i][j] = 0
      blown_ball_pos = [(x,y)]
      count = 1
      prev = board[x][y]
    
  if count >= 4:
    blown_ball.append((board[blown_ball_pos[-1][0]][blown_ball_pos[-1][1]], count))
    for x, y in blown_ball_pos:
      board[x][y] = 0
  return total_count
    
def make_group():
  prev = -1
  count = 1
  new_order = deque([])
  for x, y in rotate_pos_order:
    if prev == -1:
      prev = board[x][y]
      count = 0
      
    if board[x][y] == prev:
      count += 1
    else:
      new_order.append(count)
      new_order.append(prev)
      prev = board[x][y]
      count = 1
  return new_order
      
def update_board():
  new_order = make_group()
  for x, y in rotate_pos_order:
    if len(new_order) == 0:
      board[x][y] = 0
    else:
      board[x][y] = new_order.popleft()

def print_board():
  for i in range(n):
    for j in range(n):
      print(board[i][j], end=' ')
    print()

get_rotate_pos_order() # O(n^2)
for magic_dir, magic_distance in magic: # O(m)
  use_magic(magic_dir, magic_distance) # O(1)
  move_balls() # O(n^2)
  while blowup_ball() > 0:
    move_balls()
  update_board() # O(n^2)

answer = 0
for ball, count in blown_ball:
  answer += ball * count
print(answer)