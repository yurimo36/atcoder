# https://atcoder.jp/contests/abc014/tasks/abc014_1

a = int(input())
b = int(input())

if a == b:
  print(0)
elif a < b:
  print(b-a)
else:
  print(b-a%b)