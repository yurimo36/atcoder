# https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_b

s = list(input())
ans = 0

for i in range(len(s)):
  if i%2 == 0:
    ans += int(s[i])
  else:
    ans -= int(s[i])

print(ans)