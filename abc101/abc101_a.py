# https://atcoder.jp/contests/abc101/tasks/abc101_a

s = list(input())
ans = 0

for c in s:
  if c == "+":
    ans += 1
  else:
    ans -= 1

print(ans)