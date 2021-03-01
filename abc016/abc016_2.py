# https://atcoder.jp/contests/abc016/tasks/abc016_2

a, b, c = map(int,input().split())

x = a + b
y = a - b

if c == x and c == y:
  print("?")
elif c != x and c == y:
  print("-")
elif c == x and c != y:
  print("+")
else:
  print("!")