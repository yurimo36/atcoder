# https://atcoder.jp/contests/abc169/tasks/abc169_b

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
ans = 1

if li.count(0) > 0:
    print(0)
    exit()

for i in li:
    ans = ans * i
    if ans > 10**18:
        print(-1)
        exit()

print(ans)
