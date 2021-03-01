# https://atcoder.jp/contests/abc003/tasks/abc003_1

n = int(input())
ans = 0.0

for i in range(1,n+1):
  ans = ans + i * 10000 / n

print(ans)