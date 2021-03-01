# https://atcoder.jp/contests/abc166/tasks/abc166_b

import itertools

n, k = map(int,input().split())
li = []

for i in range(k):
    x = int(input())
    li.append(list(map(int,input().split())))

li = list(itertools.chain.from_iterable(li))
li = set(li)

print(n-len(li))