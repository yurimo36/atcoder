# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b

x, y = map(int,input().split())

if x==1 or y==1:
  print(1)
else:
  print((x*y+1)//2)