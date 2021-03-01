# https://atcoder.jp/contests/abc143/tasks/abc143_a

a,b = map(int,input().split())

ans = a - b * 2
if ans < 0:
  ans = 0

print(ans)