# https://atcoder.jp/contests/abc064/tasks/abc064_a

x, y, z = map(int,input().split())
if (10*y+z)%4 == 0:
  print("YES")
else:
  print("NO")