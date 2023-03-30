import sys
from collections import defaultdict

n = int(sys.stdin.readline())
graph = defaultdict(set)
all_nodes = set()
answer = list()

for _ in range(n):
  a, b = sys.stdin.readline().rstrip().split(' => ')
  graph[a].add(b)
  all_nodes.add(a)
  all_nodes.add(b)

def floyd_warshall(graph):
  for k in all_nodes:
    for i in all_nodes:
      for j in all_nodes:
        if k in graph[i] and j in graph[k]:
          graph[i].add(j)
  return graph

floyd_warshall(graph)

for i in sorted(graph.keys()):
  for j in sorted(graph[i]):
    if i != j:
      answer.append(f'{i} => {j}')
print(len(answer))
print('\n'.join(answer))