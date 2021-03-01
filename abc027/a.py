# https://atcoder.jp/contests/abc027/tasks/abc027_a

li = list(map(int,input().split()))
for i in li:
  if li.count(i) == 1 or li.count(i) == 3:
    print(i)
    exit()