#백준 17626번

n = int(input())

is_square = [False]*50001
square = []

i = 1
while i*i <= 50000:
  is_square[i*i] = True
  square.append(i*i)
  i += 1
  
def check(n):
  if is_square[n]:
    return 1
  m = len(square)
  for i in range(m):
    if square[i] > n:
      break
    if is_square[n-square[i]]:
      return 2
  
  for i in range(m):
    for j in range(i, m):
      if square[i] + square[j] > n:
        break
      if is_square[n-square[i]-square[j]]:
        return 3
  return 4
print(check(n))

