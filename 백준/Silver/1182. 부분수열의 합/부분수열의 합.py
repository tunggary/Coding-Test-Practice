import sys

n,s = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = 0

def backtracking(sum, idx):
  global answer
  if sum == s:
    answer += 1

  for i in range(idx, n):
    backtracking(sum+array[i], i+1)

backtracking(0, 0)
print(answer-1 if s == 0 else answer)