# https://atcoder.jp/contests/tenka1-2012-qualC/tasks/tenka1_2012_9

import math

n = int(input())
ans = 0

def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

for i in range(2,n):
    if is_prime(i):
        ans += 1

print(ans)