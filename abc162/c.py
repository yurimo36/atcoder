# https://atcoder.jp/contests/abc162/tasks/abc162_c

import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

k = int(input())
ans = 0

for i in range(1,k+1):
    ans += i #数1種類
    for j in range(i+1,k+1):
        ans += gcd(i,j) * 6 #数2種類
        for k in range(j+1,k+1):
            ans += gcd(i, j, k) * 6 #数3種類
    
print(ans)