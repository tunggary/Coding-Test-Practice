import sys

n,m = map(int, sys.stdin.readline().split())
print("<", end="")
nodes = dict()
for i in range(1, n+1):
  if i == 1:
    nodes[i] = {"num": i, "left": n, "right": i + 1}
  elif i == n:
    nodes[i] = {"num": i, "left": i - 1, "right": 1}
  else:
    nodes[i] = {"num": i, "left": i - 1, "right": i + 1}
    
current = 1
count = 0
while True:
  if count < m - 1:
    count += 1
    current = nodes[current]["right"]
    continue
  if len(nodes) == 1:
    print(nodes[current]["num"], end="")
    break
  else:
    print(nodes[current]["num"], end=", ")
  count = 0
  nodes[nodes[current]["left"]]["right"] = nodes[current]["right"]
  nodes[nodes[current]["right"]]["left"] = nodes[current]["left"]
  temp = nodes[current]["right"]
  del nodes[current]
  current = temp
  
print(">")
