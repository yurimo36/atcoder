# https://atcoder.jp/contests/abc083/tasks/abc083_a

a, b, c, d = map(int,input().split())
if a+b > c+d:
  print("Left")
if a+b < c+d:
  print("Right")
if a+b == c+d:
  print("Balanced")