# https://atcoder.jp/contests/abc196/tasks/abc196_c

n = int(input())
x = len(str(n))
ans = 0

for i in range(1,x):
  if i%2 == 0:
    ans += 9 * 10**(i//2-1)

if x%2 == 0:
  for i in range(10**(x//2-1), 10**(x//2)):
    y = int(str(i)+str(i))
    if y <= n:
      ans += 1
    else:
      break

print(ans)
