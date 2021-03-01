# https://atcoder.jp/contests/abc121/tasks/abc121_b

n, m, c = map(int,input().split())
b = list(map(int,input().split()))
ans = 0

for i in range(n):
  a = list(map(int,input().split()))
  x = 0
  for j in range(m):
    x += b[j]*a[j]
  if x + c > 0:
    ans += 1

print(ans)