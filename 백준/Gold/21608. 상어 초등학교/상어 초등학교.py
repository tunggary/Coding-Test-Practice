import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().strip())
favorite = {}
student_order = []
empty_desks = []
classroom = [[0] * n for _ in range(n)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for _ in range(n**2):
  input = list(map(int, sys.stdin.readline().strip().split()))
  favorite[input[0]] = input[1:]
  student_order.append(input[0])
  
for i in range(n):
  for j in range(n):
    empty_desks.append((i, j))
    
def get_answer():
  answer = 0
  for i in range(n):
    for j in range(n):
      count = 0
      for dx, dy in dir:
        nx = i + dx
        ny = j + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
          continue
        for favorite_student in favorite[classroom[i][j]]:
          if classroom[nx][ny] == favorite_student:
            count += 1
      answer += 10 ** (count - 1) if count > 0 else 0
  return answer

def find(student):
  heap = []
  for desk in empty_desks:
    empty_count = 0
    favorite_count = 0
    position = (desk[0], desk[1])
    for dx, dy in dir:
      nx = desk[0] + dx
      ny = desk[1] + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if classroom[nx][ny] == 0:
        empty_count += 1
        continue
      for favorite_student in favorite[student]:
        if classroom[nx][ny] == favorite_student:
          favorite_count += 1
    heappush(heap, (-favorite_count, -empty_count, position))
  
  x, y = heappop(heap)[2]
  classroom[x][y] = student
  empty_desks.remove((x,y))

for student in student_order:
  find(student)
  
print(get_answer())