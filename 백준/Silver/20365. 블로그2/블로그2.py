import sys

n = int(sys.stdin.readline().strip())
order = sys.stdin.readline().strip()

count = { "R": 0, "B": 0 }
prev_color = ''
for current in order:
  if current != prev_color:
    count[current] += 1
    prev_color = current
    
print(min(count["B"], count["R"])+1)