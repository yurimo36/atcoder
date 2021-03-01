# https://atcoder.jp/contests/abc063/tasks/abc063_b

import collections

s = list(input())
c = collections.Counter(s)

if c.most_common()[0][1] == 1:
    print("yes")
else:
    print("no")