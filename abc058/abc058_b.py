# https://atcoder.jp/contests/abc058/tasks/abc058_b

s = input()
t = input()
ans = ""

for i in range(min(len(s),len(t))):
  ans = ans + s[i] + t[i]

if len(s) > i+1:
  ans = ans + s[i+1:]
elif len(t) > i+1:
  ans = ans + t[i+1:]

print(ans)