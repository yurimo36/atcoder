# https://atcoder.jp/contests/abc195/tasks/abc195_c

n = int(input())
x = len(str(n))
y = 1
ans = 0

for i in range(4, 16):
  if x > i:
    ans += 9 * y * 10**(i-1)
    if i%3 == 0:
      y += 1
  else:
    break

if x > 3:
  ans += (n - 10**(x-1) + 1) * y

print(ans)
