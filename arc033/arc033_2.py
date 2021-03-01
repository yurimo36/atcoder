# https://atcoder.jp/contests/arc033/tasks/arc033_2

import collections

x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = len(set(a+b))
x = 0
y = 0
ans = 0
ca = collections.Counter(a)
cb = collections.Counter(b)

for i in ca.keys():
    if i in cb.keys():
        ans += 1

print(ans/c)