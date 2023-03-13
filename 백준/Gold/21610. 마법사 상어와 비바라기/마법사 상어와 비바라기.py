import sys

# 구름 이동
# 비 내림
# 물 복사
# 구름 생성

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
command = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
clouds = set([(n-1,0), (n-1,1), (n-2,0), (n-2,1)])

for dir, dis in command:
  dx, dy = move[dir-1]
  move_clouds = set()
  # 구름 이동
  for x,y in clouds:
    nx, ny = (x+dx*dis)%n, (y+dy*dis)%n
    move_clouds.add((nx,ny))
    # 비 내림
    graph[nx][ny] += 1
  # 물 복사
  for x,y in move_clouds:
    for j in range(1, 8, 2):
      nx, ny = x+move[j][0], y+move[j][1]
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
        graph[x][y] += 1
  # 구름 생성
  new_clouds = set()
  for i in range(n):
    for j in range(n):
      if (i,j) not in move_clouds and graph[i][j] >= 2:
        new_clouds.add((i,j))
        graph[i][j] -= 2
  clouds = new_clouds

print(sum(map(sum, graph)))