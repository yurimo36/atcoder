# https://atcoder.jp/contests/abc147/tasks/abc147_b

s = input()
ans = 0

for i in range (int(len(s)/2)):
  if s[i] == s[-i-1]:
    continue
  else:
    ans = ans + 1

print(ans)