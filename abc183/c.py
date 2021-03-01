# https://atcoder.jp/contests/abc183/tasks/abc183_c

import itertools

n, k = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]
ans = 0

for v in itertools.permutations([i+1 for i in range(n-1)], n-1):
    junban = [0] + list(v) + [0]
    x = 0
    for i in range(n):
        x += li[junban[i]][junban[i+1]]
    if x == k:
        ans += 1

print(ans)
