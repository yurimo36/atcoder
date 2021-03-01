# https://atcoder.jp/contests/abc028/tasks/abc028_c

import itertools

li = list(map(int,input().split()))
c_list = list(itertools.combinations(li, 3))
ans = []

for x in c_list:
    ans.append(sum(x))

ans.sort(reverse=True)
print(ans[2])