# https://atcoder.jp/contests/abc112/tasks/abc112_b

n, t = map(int,input().split())
ans = []

for i in range(n):
  c, x = map(int,input().split())
  if x <= t:
    ans.append(c)

if len(ans) == 0:
    print("TLE")
else:
    ans.sort()
    print(ans[0])