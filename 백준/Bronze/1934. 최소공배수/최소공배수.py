import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    print(math.lcm(n, m))