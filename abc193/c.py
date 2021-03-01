# https://atcoder.jp/contests/abc193/tasks/abc193_c

import math

n = int(input())
li = []

for i in range(2,10**5):
    for j in range(2, 40):
        x = i**j
        if x > n:
            break
        li.append(x)

print(n-len(set(li)))
