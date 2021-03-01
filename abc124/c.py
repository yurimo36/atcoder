# https://atcoder.jp/contests/abc124/tasks/abc124_c

s = input()
ans = 0
t = "01" * len(s)

for i in range(len(s)):
  if s[i] != t[i]:
    ans = ans + 1  
  
print(min(ans, abs(len(s)-ans)))