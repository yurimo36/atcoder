# https://atcoder.jp/contests/abc017/tasks/abc017_1

ans = 0

for i in range(3):
  x,y = map(int,input().split())
  ans = ans + int(x*y/10)

print(ans)