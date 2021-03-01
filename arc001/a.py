# https://atcoder.jp/contests/arc001/tasks/arc001_1

import collections

n = int(input())
li = list(input())
c = collections.Counter(li)

if len(c.most_common()) == 4:
    print(c.most_common()[0][1], c.most_common()[-1][1])
else:
    print(c.most_common()[0][1], 0)