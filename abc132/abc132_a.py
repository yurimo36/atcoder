# https://atcoder.jp/contests/abc132/tasks/abc132_a

import collections

s = list(input())
c = collections.Counter(s)

if len(c) == 2 and c.most_common()[0][1] == 2:
  print("Yes")
else:
  print("No")