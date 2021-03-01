# https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a

import copy

n = int(input())
li = list(map(int,input().split()))
x = max(li)
y = sum(li)

#累積和を計算
for i in range(n-1):
    li[i+1] += li[i]
li = [0] + li

for i in range(1,n+1):
    ans = 0
    for j in range(n-i+1):
        x = li[j+i] - li[j]
        if x > ans:
            ans = x
    print(ans)