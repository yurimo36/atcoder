# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_b

import collections
import itertools

li = [list(map(int,input().split())) for i in range(3)]
li = list(itertools.chain.from_iterable(li))
li.sort()

c = list(collections.Counter(li).values())

if c.count(2) == 2 and c.count(1) == 2:
    print("YES")
else:
    print("NO")