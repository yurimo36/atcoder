# https://atcoder.jp/contests/abc082/tasks/arc087_a

import collections

n = int(input())
li = list(map(int,input().split()))
c = collections.Counter(li)
ans = 0

for item in c.items():
    x = item[0] #要素
    y = item[1] #個数

    if x < y:
        ans += y-x

    if x > y:
        ans += y

print(ans)