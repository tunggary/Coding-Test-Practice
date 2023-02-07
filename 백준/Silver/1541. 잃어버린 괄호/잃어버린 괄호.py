import sys

exp = sys.stdin.readline().strip()
exp_list = []
num = ''
for i in range(len(exp)):
  if exp[i].isdigit():
    num += exp[i]
  else:
    if num != '':
      exp_list.append(int(num))
      num = ''
    exp_list.append(exp[i])
exp_list.append(int(num))

answer = 0
is_minus = False

for i in range(len(exp_list)):
  if exp_list[i] == '-':
    is_minus = True
  elif exp_list[i] == '+':
    continue
  else:
    if is_minus:
      answer -= exp_list[i]
    else:
      answer += exp_list[i]
   
print(answer)