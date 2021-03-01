# https://atcoder.jp/contests/abc047/tasks/abc047_a

li = list(map(int,input().split()))

if sum(li) == 2*max(li):
  print("Yes")
else:
  print("No")