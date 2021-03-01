# https://atcoder.jp/contests/abc035/tasks/abc035_c

import collections

n, q = map(int,input().split())
ans = [0]*n

for i in range(q):
    l, r = map(int,input().split())
    ans[l-1] += 1
    if r == n:
        continue
    ans[r] -= 1

for i in range(n-1):
    ans[i+1] += ans[i]

for i in range(n):
    if ans[i]%2 == 0:
        print(0,end="")
    else:
        print(1,end="")
print()