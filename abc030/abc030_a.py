# https://atcoder.jp/contests/abc030/tasks/abc030_a

a, b, c, d = map(int,input().split())

if b/a == d/c:
  print("DRAW")
elif b/a < d/c:
  print("AOKI")
else:
  print("TAKAHASHI")