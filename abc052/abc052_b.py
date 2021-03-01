# https://atcoder.jp/contests/abc052/tasks/abc052_b

n = int(input())
s = input()
x = 0
ans = 0

for c in s:
  if c == "I":
    x += 1
  else:
    x -= 1
  if x > ans:
    ans = x

print(ans)