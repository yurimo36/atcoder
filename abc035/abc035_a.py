# https://atcoder.jp/contests/abc035/tasks/abc035_a

x, y = map(int,input().split())

if x/y > 1.5:
  print("16:9")
else:
  print("4:3")