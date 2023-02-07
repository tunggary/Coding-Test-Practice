import sys

n = int(sys.stdin.readline().strip())

five = n // 5
two = (n % 5) // 2
change = (n % 5) % 2 

while change != 0:
  if five == 0:
    break
  five -= 1
  two += (5 + change) // 2
  change = (5 + change) % 2
  
print(five + two if change == 0 else -1)