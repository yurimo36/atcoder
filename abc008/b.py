# https://atcoder.jp/contests/abc008/tasks/abc008_2

import collections

n = int(input())
s = [input() for i in range(n)]
c = collections.Counter(s)

print(c.most_common()[0][0])