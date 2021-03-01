# https://atcoder.jp/contests/abc032/tasks/abc032_a

import fractions

a = int(input())
b = int(input())
n = int(input())

d = fractions.gcd(a,b)
c = a*b//d

if n%c == 0:
  print(n)
else:
  print(c*(n//c + 1))