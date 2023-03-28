import sys
from collections import defaultdict

n = int(sys.stdin.readline())
mapping = defaultdict(int)

for _ in range(n):
  file = sys.stdin.readline().rstrip()
  extention = file.split('.')[-1]
  mapping[extention] += 1

print('\n'.join([f'{key} {value}' for key, value in sorted(mapping.items())]))