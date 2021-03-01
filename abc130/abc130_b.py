# https://atcoder.jp/contests/abc130/tasks/abc130_b

n, x = map(int,input().split())
l = list(map(int,input().split()))
y = 0
ans = 1

for i in l:
  y = y + i
  if y <= x:
    ans = ans + 1

print(ans)  