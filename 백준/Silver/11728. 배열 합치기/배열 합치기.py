import sys

n,m = map(int, sys.stdin.readline().split())
array1 = list(map(int, sys.stdin.readline().split()))
array2 = list(map(int, sys.stdin.readline().split()))

for i in sorted(array1 + array2):
  print(i, end=" ")