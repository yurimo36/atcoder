# https://atcoder.jp/contests/arc044/tasks/arc044_a

import math

n = int(input())

if n == 1:
    print("Not Prime")
    exit()

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

if is_prime(n):
    print("Prime")
    exit()

if n%3 != 0 and n%2 != 0 and n%5 != 0:
    print("Prime")

else:
    print("Not Prime")