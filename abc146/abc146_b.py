# https://atcoder.jp/contests/abc146/tasks/abc146_b

n = int(input())
s = input()
x = 0
ans = ""
c = ""

for i in s:
  x = ord(i) + n
  if x > 90:
      x = x - 26
  c = chr((x))
  ans = ans + c

print(ans)