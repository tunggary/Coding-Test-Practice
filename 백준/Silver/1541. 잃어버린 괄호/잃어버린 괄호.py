import sys

def get_sum(exp):
  return sum(map(int, exp.split('+')))

exp = sys.stdin.readline().strip().split('-')
answer = int(get_sum(exp[0]))
for i in range(1, len(exp)):
  answer -= get_sum(exp[i])
  
print(answer)