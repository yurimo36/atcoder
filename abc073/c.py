# https://atcoder.jp/contests/abc073/tasks/abc073_c

import collections

n = int(input())
li = [int(input()) for i in range(n)]
c = collections.Counter(li)
ans = 0

for item in c.items():
    if item[1]%2 == 1:
        ans += 1

print(ans)