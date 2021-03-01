# https://atcoder.jp/contests/abc026/tasks/abc026_b

import math

n = int(input())
r = [int(input()) for i in range(n)]
r.sort()
ans = 0

for i in range(n):
  if i%2 == 0:
    ans += r[i]**2
  else:
    ans -= r[i]**2

print(abs(ans*math.pi))