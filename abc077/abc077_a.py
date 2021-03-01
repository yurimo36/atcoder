# https://atcoder.jp/contests/abc077/tasks/abc077_a

s = list(input())
t = list(input())

if s[0]==t[2] and s[1]==t[1] and s[2]==t[0]:
  print("YES")
else:
  print("NO")