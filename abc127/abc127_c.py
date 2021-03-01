# https://atcoder.jp/contests/abc127/tasks/abc127_c

n, m = map(int,input().split())
l, r = map(int,input().split())

for i in range(m-1):
  a, b = map(int,input().split())
  if a > l:
    l = a
  if b < r:
    r = b

ans = r - l + 1
if ans<0:
    print(0)
else:
    print(ans)