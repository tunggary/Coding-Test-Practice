import sys

n = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
min_budget = 0
max_budget = max(budgets)
sum_budget = sum(budgets)
answer = max_budget

def get_sum(max_budget):
  sum = 0
  for budget in budgets:
    sum += min(budget, max_budget)
  return sum

if sum_budget <= m:
  print(max_budget)
else:
  prev_middle = -1
  while min_budget < max_budget:
    middle = (min_budget + max_budget) // 2
    if prev_middle == middle:
      break
    prev_middle = middle
    middle_sum = get_sum(middle)
    if middle_sum <= m:
      min_budget = middle
      answer = middle
    else:
      max_budget = middle
  print(answer)