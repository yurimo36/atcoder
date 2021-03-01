# https://atcoder.jp/contests/abc089/tasks/abc089_c

import itertools

n = int(input())
li = [0]*5
ans = 0

for i in range(n):
    s = input()
    if s[0] == "M":
        li[0] = li[0] + 1
    if s[0] == "A":
        li[1] = li[1] + 1
    if s[0] == "R":
        li[2] = li[2] + 1
    if s[0] == "C":
        li[3] = li[3] + 1
    if s[0] == "H":
        li[4] = li[4] + 1

for l in itertools.combinations(li, 3):
    ans += l[0] * l[1] * l[2]    

print(ans)