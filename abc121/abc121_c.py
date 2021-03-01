# https://atcoder.jp/contests/abc121/tasks/abc121_c

n, m = map(int,input().split())
ans = 0
ab = []
for i in range(n):
  ab.append(list(map(int,input().split())))
ab.sort()

i = 0
while m > 0:
  if m > ab[i][1]:
    ans = ans + ab[i][0]*ab[i][1]
  else:
    ans = ans + ab[i][0]*m
  m -= ab[i][1]
  i += 1

print(ans)