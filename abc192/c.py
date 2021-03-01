# https://atcoder.jp/contests/abc192/tasks/abc192_c

n, k = map(int,input().split())
ans = n

def g1(x):
  y = ''.join(sorted(list(x), reverse=True))
  return int(y)

def g2(x):
  y = ''.join([n for n in sorted(list(x)) if n!='0'])
  return int(y)

def f(x):
  return g1(str(x)) - g2(str(x))

for i in range(k):
  ans = f(ans)
  if ans == 0:
    break

print(ans)
