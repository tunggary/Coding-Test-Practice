#백준 1074번
#아이디어: dfs를 만족하는 범위 내에서만 진행

import sys
n,r,c = map(int, sys.stdin.readline().split())

#len: 정사각형 길이
#count: 원소 하나의 들어갈 숫자
def dfs(len,count,row,col):
  global r,c
  if len == 1:
    if row == r and col == c:
      print(count)
  else:
    half = len//2
    addCount = (len//2)**2
    center_row = row + half
    center_col = col + half
    if r < center_row and c < center_col:
      dfs(half,count+addCount*0,row,col)
    if r < center_row and c >= center_col:
      dfs(half,count+addCount*1,row,col+half)
    if r >= center_row and c < center_col:
      dfs(half,count+addCount*2,row+half,col)
    if r >= center_row and c >= center_col:
      dfs(half,count+addCount*3,row+half,col+half)
      
dfs(2**n,0,0,0)
