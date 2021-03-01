# https://atcoder.jp/contests/abc156/tasks/abc156_b

n, k = map(float,input().split())
i=0

while n>=1:
  n = n/k
  i = i+1

print(i)