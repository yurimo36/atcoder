# https://atcoder.jp/contests/abc192/tasks/abc192_b

s = list(input())

s0 = ''.join(s[0::2])
s1 = ''.join(s[1::2])

if s0.islower() and (s1.isupper() or s1 == ''):
  print("Yes")
else:
  print("No")
