# https://atcoder.jp/contests/abc194/tasks/abc194_a

x, y = map(int,input().split())
x += y

if x >= 15 and y >= 8:
  print(1)
elif x >= 10 and y >= 3:
  print(2)
elif x >= 3:
  print(3)
else:
  print(4)
