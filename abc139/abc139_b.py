# https://atcoder.jp/contests/abc139/tasks/abc139_b

a, b = map(int,input().split())
x = 1
ans = 0

while x < b:
  x = x + a - 1
  ans = ans + 1

print(ans)