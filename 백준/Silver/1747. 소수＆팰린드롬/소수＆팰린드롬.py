import sys
n = int(sys.stdin.readline().strip())
    
def is_palindrome(num):
  num = str(num)
  for i in range(len(num)//2):
    if num[i] != num[-i-1]:
      return False
  return True

def is_prime(num):
  if num == 1:
    return False
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True
    
while True:
  if is_palindrome(n) and is_prime(n):
    print(n)
    break
  n += 1
