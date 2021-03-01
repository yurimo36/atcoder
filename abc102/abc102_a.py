# https://atcoder.jp/contests/abc102/tasks/abc102_a

import fractions

n = int(input())
print(n * 2 // fractions.gcd(2, n))