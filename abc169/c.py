# https://atcoder.jp/contests/abc169/tasks/abc169_c

import math
from decimal import Decimal

li = input().split()
x = Decimal(li[0]) * Decimal(li[1])

print(math.floor(x))