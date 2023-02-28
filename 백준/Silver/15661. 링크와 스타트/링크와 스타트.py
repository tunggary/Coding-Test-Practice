import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
teams = [0]*n
answer = 1_000_000_000

def get_team_score():
  global answer
  start = 0
  link = 0
  for i in range(n-1):
    for j in range(i+1,n):
      if teams[i] == 1 and teams[j] == 1:
        start += graph[i][j] + graph[j][i]
      elif teams[j] == 0 and teams[i] == 0:
        link += graph[i][j] + graph[j][i]
  answer = min(answer, abs(start - link))

def separate_team(iter):
  if iter == n:
    get_team_score()
    return
  
  teams[iter] = 1
  separate_team(iter+1)
  teams[iter] = 0
  separate_team(iter+1)
  
separate_team(0)
print(answer)