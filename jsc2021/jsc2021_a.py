# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_a

x, y, z = map(int,input().split())

a = y / x
b = z * a

if b.is_integer():
  print(int(b-1))
else:
  print(int(b))
