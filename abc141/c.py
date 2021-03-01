# https://atcoder.jp/contests/abc141/tasks/abc141_c

import collections

n, k, q = map(int,input().split())
A = [int(input()) for i in range(q)]
c = collections.Counter(A)

for i in range(1,n+1):
  if c[i] >= q-k+1 :
    print("Yes")
  else:
    print("No")