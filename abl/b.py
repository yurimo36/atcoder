# https://atcoder.jp/contests/abl/tasks/abl_b

a, b, c, d = map(int,input().split())

if a <= b < c or c <= d < a:
  print("No")
else:
  print("Yes")
