# https://atcoder.jp/contests/abc155/tasks/abc155_c

import collections

n = int(input())
s = [input() for i in range(n)]
c = collections.Counter(s)
x = c.most_common()[0][1]

s = list(set(s))
s.sort()

for item in s:
  if c[item] == x:
  	print(item)