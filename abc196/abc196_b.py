# https://atcoder.jp/contests/abc196/tasks/abc196_b

s = input()
x = len(s)

for i in range(len(s)):
  if s[i] == ".":
    x = i

print(s[:x])
