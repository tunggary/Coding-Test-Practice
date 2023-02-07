import sys

board = sys.stdin.readline().strip()

board_list = board.split('.')

for i in range(len(board_list)):
  if board_list[i] == '':
    continue
  
  board_list[i] = board_list[i].replace('XXXX', 'AAAA')
  board_list[i] = board_list[i].replace('XX', 'BB')
  if 'X' in board_list[i]:
    print(-1)
    exit(0)

print('.'.join(board_list))