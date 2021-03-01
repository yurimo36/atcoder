# https://atcoder.jp/contests/abc124/tasks/abc124_a

x, y = map(int,input().split())

if x == y:
  ans = x * 2
elif x > y:
  ans = 2*x - 1
else:
  ans = 2*y - 1

print(ans)