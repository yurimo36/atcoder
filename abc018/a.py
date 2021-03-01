# https://atcoder.jp/contests/abc018/tasks/abc018_1

a = int(input())
b = int(input())
c = int(input())

if a > b and b > c:
  print(1)
  print(2)
  print(3)
elif a > c and c > b:
  print(1)
  print(3)
  print(2)
elif b > a and a > c:
  print(2)
  print(1)
  print(3)
elif b > c and c > a:
  print(3)
  print(1)
  print(2)
elif c > a and a > b:
  print(2)
  print(3)
  print(1)
else:
  print(3)
  print(2)
  print(1)