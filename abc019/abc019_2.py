# https://atcoder.jp/contests/abc019/tasks/abc019_2

s = input()
ans = ""
x = 1
c = ""

for i in range(len(s)):
  c = s[i]
  if i + 1 == len(s):
    ans = ans + c + str(x)
    x = 1
  elif s[i] == s[i+1]:
    x = x + 1
  else:
    ans = ans + c + str(x)
    x = 1
  
print(ans)