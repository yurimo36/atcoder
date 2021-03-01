# https://atcoder.jp/contests/abc137/tasks/abc137_c

import collections
from math import factorial

def combinations_count(n, r): #組み合わせ
    return factorial(n) // (factorial(n - r) * factorial(r))

n = int(input())
li = []
ans = 0

for i in range(n):
    s = list(input())
    s.sort()
    li.append(''.join(s))

c = list(collections.Counter(li).values())
c.sort(reverse=True)

for i in c:
    if i == 1:
        break
    ans += combinations_count(i, 2)

print(ans)