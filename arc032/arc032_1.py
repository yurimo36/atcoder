# https://atcoder.jp/contests/arc032/tasks/arc032_1

import math

n = int(input())
x = 0

for i in range(1,n+1):
    x += i

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

if is_prime(x):
    print("WANWAN")
else:
    print("BOWWOW")