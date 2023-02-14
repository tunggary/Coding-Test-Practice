import sys

n = int(sys.stdin.readline().strip())

def is_square(num):
  if num <= 0 or num != int(num**0.5)**2:
    return False
  else:
    return True

def find(num):
  if is_square(num):
    return 1
  
  for i in range(1, int(num**0.5)+1):
    if is_square(num-i**2):
      return 2
    
  for i in range(1, int(num**0.5)+1):
    for j in range(1, int(num**0.5)+1):
      if is_square(num - i**2 - j**2):
        return 3
      
  return 4

print(find(n))