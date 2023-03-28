import sys
import re

n = int(sys.stdin.readline())
p = re.compile(r'^[A-F]?A+F+C+[A-F]?$')

for _ in range(n):
  if p.match(sys.stdin.readline().rstrip()):
    print('Infected!')
  else:
    print('Good')