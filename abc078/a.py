# https://atcoder.jp/contests/abc078/tasks/abc078_a

s = list(input())

if s[0] == s[2]:
  print("=")
elif s[0] < s[2]:
  print("<")
else:
  print(">")