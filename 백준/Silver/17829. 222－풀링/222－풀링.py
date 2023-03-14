import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def divide_conquer(graph, n):
  if n == 1:
    return graph[0][0]
  new_graph = [[0] * (n//2) for _ in range(n//2)]
  for i in range(0, n, 2):
    for j in range(0, n, 2):
      new_graph[i//2][j//2] = sorted([graph[i][j], graph[i][j+1], graph[i+1][j], graph[i+1][j+1]])[2]
  return divide_conquer(new_graph, n//2)

print(divide_conquer(graph, n))