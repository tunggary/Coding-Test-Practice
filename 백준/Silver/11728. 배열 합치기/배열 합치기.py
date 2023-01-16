import sys

n,m = sys.stdin.readline().split()
list1 = list(map(int, sys.stdin.readline().split()))
list2 = list(map(int, sys.stdin.readline().split()))

i,j = 0,0

while i < len(list1) and j < len(list2):
  if list1[i] < list2[j]:
    print(list1[i], end=" ")
    i += 1
  else:
    print(list2[j], end=" ")
    j += 1

while i < len(list1):
  print(list1[i], end=" ")
  i += 1

while j < len(list2):
  print(list2[j], end=" ")
  j += 1