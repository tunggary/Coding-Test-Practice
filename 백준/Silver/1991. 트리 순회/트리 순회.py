import sys

sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline().strip())

graph = dict()

for _ in range(n):
  parent, child1, child2 = sys.stdin.readline().strip().split()
  graph[parent] = {
    "left": child1,
    "right": child2
  }
  
def preorder(node):
  if node == '.':
    return
  print(node, end='')
  preorder(graph[node]["left"])
  preorder(graph[node]["right"])

def inorder(node):
  if node == '.':
    return
  inorder(graph[node]["left"])
  print(node, end='')
  inorder(graph[node]["right"])

def postorder(node):
  if node == '.':
    return
  postorder(graph[node]["left"])
  postorder(graph[node]["right"])
  print(node, end='')
  
preorder("A")
print()
inorder("A")
print()
postorder("A")
print()