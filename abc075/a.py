# https://atcoder.jp/contests/abc075/tasks/abc075_a

a, b, c = map(int,input().split())

if a==b:
  print(c)
if b==c:
  print(a)
if a==c:
  print(b)