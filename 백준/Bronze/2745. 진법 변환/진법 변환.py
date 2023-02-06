import sys

number, base = sys.stdin.readline().strip().split()

print(int(number, int(base)))