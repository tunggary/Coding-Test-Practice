import sys

n = int(sys.stdin.readline())
input = []
for _ in range(n):
  input.append(int(sys.stdin.readline()))

stack = []
print_list = []
i = 1

for num in input:
  while i <= num:
    stack.append(i)
    print_list.append('+')
    i += 1
  if num == stack[-1]:
    stack.pop()
    print_list.append('-')

print("NO" if len(stack) != 0 else '\n'.join(print_list))