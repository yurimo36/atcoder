# https://atcoder.jp/contests/abc127/tasks/abc127_a

a, b = map(int,input().split())
 
if a > 12:
  print(b)
elif a > 5:
  print(int(b/2))
else:
  print(0)