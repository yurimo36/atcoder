# https://atcoder.jp/contests/abc070/tasks/abc070_c

import fractions
from functools import reduce
 
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)
 
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
 
n = int(input())
t = [int(input()) for i in range(n)]
 
print(lcm(*t))