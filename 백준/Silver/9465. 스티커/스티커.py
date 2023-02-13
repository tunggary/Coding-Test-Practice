import sys

t = int(sys.stdin.readline().strip())

def solve():
  n = int(sys.stdin.readline().strip())
  stickers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]
  for i in range(1, n):
    for j in range(2):
      if j == 0:
        stickers[j][i] = max(stickers[j][i-1], stickers[j+1][i-1]+stickers[j][i])
      else:
        stickers[j][i] = max(stickers[j][i-1], stickers[j-1][i-1]+stickers[j][i])
  print(max(stickers[0][n-1], stickers[1][n-1]))

for _ in range(t):
  solve()