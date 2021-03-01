# https://atcoder.jp/contests/arc024/tasks/arc024_1

import collections

x, y = map(int,input().split())
l = list(map(int,input().split()))
r = list(map(int,input().split()))

cl = collections.Counter(l)
cr = collections.Counter(r)

ans = 0

for l in cl.items():
    if l[0] in cr.keys():
        ans += min(l[1], cr[l[0]])

print(ans)