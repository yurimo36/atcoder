# https://atcoder.jp/contests/abc119/tasks/abc119_a

y, m, d = map(int,input().split("/"))

if y < 2020:
  if m < 5:
    print("Heisei")
  else:
    print("TBD")
else:
  print("TBD")