# https://atcoder.jp/contests/abc099/tasks/abc099_b

x, y = map(int,input().split())
z = y - x
ans = 0

for i in range(1,z):
  ans += i

print(ans-x)