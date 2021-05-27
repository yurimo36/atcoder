# https://atcoder.jp/contests/abc202/tasks/abc202_c

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = [0 for i in range(n)]

ans = 0

for i in range(n):
  x = b[c[i]-1]-1
  d[x] += 1

for i in range(n):
  ans += d[a[i]-1]

print(ans)
