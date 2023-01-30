import sys

n,m = map(int, sys.stdin.readline().split())
dogam = {}

for i in range(n):
  pocketmon = sys.stdin.readline().rstrip()
  dogam[pocketmon] = i+1
  dogam[i+1] = pocketmon
  
for _ in range(m):
  input = sys.stdin.readline().rstrip()
  if input.isdigit():
    print(dogam[int(input)])
  else:
    print(dogam[input])
