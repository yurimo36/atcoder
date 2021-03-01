# https://atcoder.jp/contests/abc148/tasks/abc148_b

n = int(input())
s, t = input().split()
ans = ""

for i in range(n):
  ans = ans + s[i] + t[i]

print(ans)