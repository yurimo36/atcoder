# https://atcoder.jp/contests/abc033/tasks/abc033_a

n = list(input())
if len(set(n)) == 1:
  print("SAME")
else:
  print("DIFFERENT")