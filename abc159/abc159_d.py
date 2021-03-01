# https://atcoder.jp/contests/abc159/tasks/abc159_d

import collections

def combinations_count(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

n = int(input())
li = list(map(int,input().split()))
c = collections.Counter(li)
ans = [0]*n
x = 0 #全てのボールから、できる組合せの総数

if len(c) == 1:
    ans = [combinations_count(n-1, 2)]*n
    print(*ans)
    exit()

for i in c.items():
    a = i[0]
    b = i[1]
    if b > 2:
        x += combinations_count(b, 2)
    elif b == 2:
        x += 1

for i in c.items():
    a = i[0]
    b = i[1]
    if b > 2:
        y = x - combinations_count(b, 2) + combinations_count(b-1, 2)
    elif b == 2:
        y = x - 1
    else:
        y = x
    ans[a-1] = y

for i in li:
    print(ans[i-1])
