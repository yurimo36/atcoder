# https://atcoder.jp/contests/abc139/tasks/abc139_a

s = input()
t = input()
ans = 0

for i in range(3):
  if s[i] == t[i]:
    ans = ans + 1

print(ans)