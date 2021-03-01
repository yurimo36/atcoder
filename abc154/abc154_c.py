# https://atcoder.jp/contests/abc154/tasks/abc154_c

import collections

n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)

if c.most_common()[0][1] == 1:
    print("YES")
else:
    print("NO")