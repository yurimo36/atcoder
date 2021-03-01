# https://atcoder.jp/contests/abc143/tasks/abc143_c

n = int(input())
s = input()
ans = len(s)

for i in range(len(s)):
  if i==0:
    continue
  else:
    if s[i] == s[i-1]:
        ans = ans - 1

print(ans)