# https://atcoder.jp/contests/abc201/tasks/abc201_a

a = list(map(int,input().split()))
a.sort()

if a[1]*2 == a[0]+a[2]:
  print("Yes")
else:
  print("No")
