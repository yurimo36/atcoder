# https://atcoder.jp/contests/abc044/tasks/abc044_b

import collections

li = list(input())
c = collections.Counter(li)

for i in c.values():
    if i%2 == 1:
        print("No")
        exit()

print("Yes")