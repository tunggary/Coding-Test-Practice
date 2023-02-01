import sys

n = int(sys.stdin.readline().strip())
parent = list(map(int, sys.stdin.readline().strip().split()))
remove_node = int(sys.stdin.readline().strip())
tree = {i:[] for i in range(n)}
root_node = 0
answer = 0

for node, parent in enumerate(parent):
  if parent == -1:
    root_node = node
    continue
  tree[parent].append(node)

def dfs(node):
  count = 0
  flag = False
  
  if len(tree[node]) == 0:
    return 1
  
  for child in tree[node]:
    if child == remove_node:
      flag = True
      continue
    count += dfs(child)
    
  return 1 if flag and count == 0 else count

if remove_node == root_node:
  print(0)
else:
  print(dfs(root_node))