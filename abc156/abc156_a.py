# https://atcoder.jp/contests/abc156/tasks/abc156_a

n, r = map(int,input().split())

if n<10:
  print(r + 100*(10-n))
else:
  print(r)
