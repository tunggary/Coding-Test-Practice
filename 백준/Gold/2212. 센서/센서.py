import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
sensors = list(map(int, sys.stdin.readline().strip().split()))
sensors.sort()
gaps = [sensors[i+1] - sensors[i] for i in range(n-1)]
gaps.sort()

print(sum(gaps[:n-k]))