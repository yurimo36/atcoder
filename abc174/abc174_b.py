# https://atcoder.jp/contests/abc174/tasks/abc174_b

n, d = map(int,input().split())
ans = 0
 
for i in range(n):
  x, y = map(int,input().split())
  z = (x**2 + y**2)**0.5
  if z <= d:
    ans += 1

print(ans)