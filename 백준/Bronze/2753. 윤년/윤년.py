import sys

n = int(sys.stdin.readline().strip())
print(int(n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)))