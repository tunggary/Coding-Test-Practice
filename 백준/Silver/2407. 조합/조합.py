import sys
import math

n,m = map(int,sys.stdin.readline().strip().split())

print(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))