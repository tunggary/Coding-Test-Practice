from itertools import combinations
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = []
all_member = set(range(1, n+1))
answer = 1_000_000_000

def get_team_score(members):
  score = 0
  if len(members) == 1:
    return 0
  for member1, members in combinations(members, 2):
    score += graph[member1-1][members-1] + graph[members-1][member1-1]
  return score

for i in range(1, n//2+1):
  for A_team in combinations(all_member, i):
    B_team = all_member - set(A_team)
    A_team_score = get_team_score(A_team)
    B_team_score = get_team_score(B_team)
    answer = min(answer, abs(A_team_score - B_team_score))
      
print(answer)