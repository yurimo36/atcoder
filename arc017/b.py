# https://atcoder.jp/contests/arc017/tasks/arc017_2

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
li = [int(input()) for i in range(n)]
x = 1
ans = []
y = 0

for i in range(1,n):
    if li[i] > li[i-1]:
        x += 1
    else:
        ans.append(x)
        x = 1
ans.append(x)

for i in ans:
    y += max(0,i-k+1)

print(y)