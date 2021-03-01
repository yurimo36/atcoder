# https://atcoder.jp/contests/abc150/tasks/abc150_c

import itertools

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
li = list(range(1, n+1))
ans = []

for i in itertools.permutations(li):
    ans.append(list(i))

print(abs(ans.index(x)-ans.index(y)))