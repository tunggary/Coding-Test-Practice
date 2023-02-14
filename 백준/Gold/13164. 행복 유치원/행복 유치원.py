import sys

n, k = map(int, sys.stdin.readline().strip().split())
children_height = list(map(int, sys.stdin.readline().strip().split()))
height_gap_sorted = sorted([children_height[i+1] - children_height[i] for i in range(n-1)])

print(sum(height_gap_sorted[:n-k]))