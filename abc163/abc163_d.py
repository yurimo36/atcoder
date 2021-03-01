# https://atcoder.jp/contests/abc163/tasks/abc163_d

import itertools

n, k = map(int,input().split())
ans = 0
li = list(range(n+1))

for i in range(k,n+2):
    a = int(1/2*i*(i-1))
    b = n*i-(int(1/2*i*(i-1)))
    ans += b - a + 1

print(ans%(10**9+7))