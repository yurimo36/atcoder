# https://atcoder.jp/contests/abc131/tasks/abc131_b

n, l = map(int,input().split())
m = list(range(l, l+n))

if 0 in m:
  print(sum(m))
  
else:
  if m[0] < 0:
    print(sum(m)-max(m))
  else:
    print(sum(m)-min(m))