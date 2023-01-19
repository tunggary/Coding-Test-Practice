import sys
expression = sys.stdin.readline().strip()

queue1 = []
queue2 = []
flag = False
for exp in expression:
  if exp == '(':
    queue1.append(exp)
    queue2.append(exp)
  elif exp == '[':
    queue1.append(exp)
    queue2.append(exp)
  elif exp == ')':
    if len(queue2) == 0 or queue2[-1] != '(' :
      flag = True
      break
    else:
      queue2.pop()
      local_sum = 0
      while queue1[-1] != '(':
        local_sum += queue1.pop()
      queue1.pop()
      queue1.append(local_sum * 2 if local_sum != 0 else 2)
  elif exp == ']':
    if len(queue2) == 0 or queue2[-1] != '[' :
      flag = True
      break
    else:
      queue2.pop()
      local_sum = 0
      while queue1[-1] != '[':
        local_sum += queue1.pop()
      queue1.pop()
      queue1.append(local_sum * 3 if local_sum != 0 else 3)
      
for q in queue1:
  if type(q) == str:
    flag = True
    break
  
print(sum(queue1) if not flag else 0)