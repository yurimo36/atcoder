# https://atcoder.jp/contests/abc072/tasks/arc082_a

import collections

n = int(input())
li = list(map(int,input().split()))
ans = []

for i in li:
    ans.append(i-1)
    ans.append(i)
    ans.append(i+1)

c = collections.Counter(ans)

print(c.most_common()[0][1])
