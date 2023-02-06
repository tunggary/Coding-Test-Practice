import sys

n = int(sys.stdin.readline().strip())

if n < 10:
  n *= 10
number = n
sum = 0
answer = 0

while number != n or answer == 0:
  sum = number//10 + number%10
  number = (number%10)*10 + sum%10
  answer += 1

print(answer)