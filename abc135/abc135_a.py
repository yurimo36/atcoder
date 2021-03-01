# https://atcoder.jp/contests/abc135/tasks/abc135_a

a, b = map(int,input().split())

if abs(a-b)%2 == 1:
  print("IMPOSSIBLE")
else:
  print(int((a+b)/2))