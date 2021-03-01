# https://atcoder.jp/contests/abc160/tasks/abc160_c

k, n = map(int,input().split())
a = list(map(int,input().split()))
d = []
x = 0

for i in range(n):
  x = abs(a[i] - a[i-1])
  if x > k/2:
    x = abs(x - k) 
  d.append(x)

print(sum(d)-max(d))