# https://atcoder.jp/contests/abc109/tasks/abc109_c

import fractions
from functools import reduce
 
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

n, x = map(int,input().split())
li = list(map(int,input().split()))
d = [abs(x-li[0])]
 
for i in range(n-1):
    d.append(abs(li[i]-li[i+1]))

print(gcd(*d))