import sys

n = int(sys.stdin.readline())  

def is_palindrome(string):
  for i in range(len(string)//2):
    if string[i] != string[-i-1]:
      return (False, i)
  return (True, 0)  
  
for _ in range(n):
  string = sys.stdin.readline().rstrip()
  check, idx = is_palindrome(string)
  if check:
    print(0)
    continue
  second_check_1, _ = is_palindrome(string[idx:-idx-1])
  second_check_2, _ = is_palindrome(string[idx+1: len(string) if idx == 0 else -idx])
  if second_check_1 or second_check_2:
    print(1)
  else:
    print(2)