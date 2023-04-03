import sys
from functools import cmp_to_key

n = int(sys.stdin.readline())
inputs = [sys.stdin.readline().rstrip() for _ in range(n)]

def parsing(string):
  ret = []
  i = 0
  while i < len(string):
    if string[i].isalpha():
      ret.append(string[i])
      i += 1
      continue
    temp = ''
    while i < len(string) and string[i].isdigit():
      temp += string[i]
      i += 1
    ret.append(temp)
  return ret

def natural_sort(string1, string2):
  parsed1 = parsing(string1)
  parsed2 = parsing(string2)
  for i in range(min(len(parsed1), len(parsed2))):
    if parsed1[i] == parsed2[i]:
      continue
    if parsed1[i].isdigit() and parsed2[i].isalpha():
      return -1
    if parsed1[i].isalpha() and parsed2[i].isdigit():
      return 1
    if parsed1[i].isalpha() and parsed2[i].isalpha():
      offset1 = ord(parsed1[i]) - ord('A') if parsed1[i].isupper() else ord(parsed1[i]) - ord('a')
      offset2 = ord(parsed2[i]) - ord('A') if parsed2[i].isupper() else ord(parsed2[i]) - ord('a')
      if offset1 == offset2:
        return -1 if parsed1[i].isupper() else 1
      else:
        return -1 if offset1 < offset2 else 1
    if parsed1[i].isdigit() and parsed2[i].isdigit():
      if int(parsed1[i]) == int(parsed2[i]):
        return -1 if len(parsed1[i]) < len(parsed2[i]) else 1
      else:
        return -1 if int(parsed1[i]) < int(parsed2[i]) else 1
  return -1 if len(parsed1) < len(parsed2) else 1
  
for string in sorted(inputs, key=cmp_to_key(natural_sort)):
  print(string)