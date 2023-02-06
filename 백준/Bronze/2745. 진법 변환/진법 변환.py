import sys

number, base = sys.stdin.readline().strip().split()
base = int(base)
answer = 0

BOUNDARY = 10 - ord('A')
length = len(number) - 1 

for i in range(len(number)):
  if number[length - i].isalpha():
    answer += (base**i)*(ord(number[length - i]) + BOUNDARY)
  else:
    answer += (base**i)*int(number[length - i])

print(answer)