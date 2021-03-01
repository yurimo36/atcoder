# https://atcoder.jp/contests/abc044/tasks/abc044_a

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b:
  print(b*c+(a-b)*d)
else:
  print(a*c)