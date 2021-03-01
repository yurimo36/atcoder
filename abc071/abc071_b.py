# https://atcoder.jp/contests/abc071/tasks/abc071_b

s = list(input())
set(s)
s.sort()
t = list("abcdefghijklmnopqrstuvwxyz")

for c in t:
  if c in s:
    continue
  else:
    print(c)
    exit()

print("None")