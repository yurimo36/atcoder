# https://atcoder.jp/contests/abc134/tasks/abc134_b

n, d = map(int,input().split())
ans = 0
x = 1 + d * 2

if n%x == 0:
  print(int(n/x))
else:
  print(int(n/x)+1)