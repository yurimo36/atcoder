# https://atcoder.jp/contests/abc083/tasks/abc083_b

n, a, b = map(int,input().split())
ans = 0

for i in range(1,n+1):
  s = str(i)
  x = 0
  for c in s:
    x += int(c)
  if a <= x <= b:
    ans += i

print(ans)