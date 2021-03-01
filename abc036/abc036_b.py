# https://atcoder.jp/contests/abc036/tasks/abc036_b

import numpy as np

n = int(input())
s = [list(input()) for i in range(n)]
s = np.rot90(np.array(s), -1)
s = list(s)

for i in s:
    for j in i:
        print(j, end ="")
    print()