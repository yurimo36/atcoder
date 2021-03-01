# https://atcoder.jp/contests/abc072/tasks/abc072_a

x,y = map(int,input().split())
if y > x:
  print(0)
else:
  print(x-y)