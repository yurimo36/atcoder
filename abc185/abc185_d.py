# https://atcoder.jp/contests/abc185/tasks/abc185_d

n, m = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
masu = []
x = 0
k = n
ans = 0

if n == m:
  print(0)
elif m == 0:
  print(1)
else:
  for i in li:
    y = i-x-1
    if y != 0:
      if y < k:
        k = y
      masu.append(y)
    x = i
  if x != m:
    masu.append(n-x)
  for i in masu:
    ans += -(-i // k)
  print(ans)
