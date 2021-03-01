# https://atcoder.jp/contests/arc015/tasks/arc015_2

import collections

n = int(input())
li = [list(map(float,input().split())) for i in range(n)]
ans = []

for l in li:
    if l[0] >=35:
        ans.append(1)
    if 35 > l[0] >= 30:
        ans.append(2)
    if 30 > l[0] >= 25:
        ans.append(3)
    if l[1] >= 25:
        ans.append(4)
    if l[1] < 0 and l[0] >= 0:
        ans.append(5)
    if l[0] < 0:
        ans.append(6)

x = []
for i in range(1,7):
    x.append(ans.count(i))

print(*x)