import sys
exp = sys.stdin.readline().strip()

prev_m_count = 0
max_result = ''
min_result = ''
for i in range(len(exp)):
  if exp[i] == 'K':
    max_result += str((10**prev_m_count)*5)
    min_result += '5' if prev_m_count == 0 else str(10**(prev_m_count-1)) + '5'
    prev_m_count = 0
  elif exp[i] == 'M':
    prev_m_count += 1
    
if prev_m_count > 0:
  max_result += '1'*prev_m_count
  min_result += str(10**(prev_m_count-1))
  
    
print(int(max_result))
print(int(min_result))
    