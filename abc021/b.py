# https://atcoder.jp/contests/abc021/tasks/abc021_b

import collections

n = int(input())
a, b = map(int,input().split())
k = int(input())
li = list(map(int,input().split())) #経由地
li = [a] + li + [b] #スタートとゴールを追加
c = collections.Counter(li)

if c.most_common()[0][1] > 1:
    print("NO")

else:
    print("YES")