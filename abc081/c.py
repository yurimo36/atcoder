# https://atcoder.jp/contests/abc081/tasks/arc086_a

import collections

x, y = map(int,input().split())
li = list(map(int,input().split()))
c = collections.Counter(li)
ans = 0

count = c.most_common()
if len(count) > y:
    for i in range(y,len(count)):
        ans += count[i][1]

print(ans)