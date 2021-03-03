# https://atcoder.jp/contests/abc185/tasks/abc185_c

import math

def combinations_count(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

l = int(input())
print(combinations_count(l-1, 11))
