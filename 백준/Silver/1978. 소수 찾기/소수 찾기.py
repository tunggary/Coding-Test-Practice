import sys

t = int(sys.stdin.readline().strip())
input_list = map(int, sys.stdin.readline().strip().split())

MAX = 1000
prime_number = [True]*(MAX+1)
prime_number[1] = False

def set_prime_number():
  for i in range(2, int(MAX**0.5)+1):
    if prime_number[i]:
      for j in range(i+i, MAX+1, i):
        prime_number[j] = False
        
set_prime_number()
print([prime_number[input] for input in input_list].count(True))  