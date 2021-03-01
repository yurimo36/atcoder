# https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_b

import collections

n, m = map(int,input().split())
li = list(map(int,input().split()))
c = collections.Counter(li)

if c.most_common()[0][1] < n//2+1:
    print("?")
else:
    print(c.most_common()[0][0])