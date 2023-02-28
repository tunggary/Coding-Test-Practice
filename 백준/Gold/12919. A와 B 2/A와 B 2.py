import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

def is_same(s, t):
  for i in range(len(s)):
    if s[i] != t[i]:
      return False
  return True

def operate2(t):
  return t[::-1][:-1]

def operate1(t):
  return t[:-1]

def dfs(t):
  if len(t) == len(s):
    if is_same(s, t):
      print(1)
      exit()
    return
  if t[-1] == 'A':
    dfs(operate1(t))
  if t[0] == 'B':
    dfs(operate2(t))
  return

dfs(t)
print(0)