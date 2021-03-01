# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_a

x = int(input())
y = int(input())
z = int(input())

a = max(x,y)
if z%a == 0:
  print(z//a)
else:
  print(z//a+1)