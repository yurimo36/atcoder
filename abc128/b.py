# https://atcoder.jp/contests/abc128/tasks/abc128_b

from operator import itemgetter

n = int(input())
sp = [input().split() for i in range(n)]

for i in range(n):
  sp[i][1] = int(sp[i][1])
  sp[i].append(i+1)

sp = sorted(sp, key=itemgetter(1), reverse=True)
sp = sorted(sp, key=itemgetter(0))

for i in range(n):
  print(sp[i][2])