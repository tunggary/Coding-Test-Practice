n = int(input())

def check(n):
  if is_sq[n] == True:
    return 1
  m = len(sq)
  for i in range(m):
    if sq[i] > n:
      break
    if is_sq[n-sq[i]]:
      return 2
    
  for i in range(m):
    for j in range(i, m):
      if sq[i] + sq[j] > n:
        break
      if is_sq[n-sq[i]-sq[j]]:
        return 3
  return 4

is_sq = [False]*50001
sq = []
i=1
while i*i<=50000:
  is_sq[i*i] = True
  sq.append(i*i)
  i+=1
  
print(check(n))