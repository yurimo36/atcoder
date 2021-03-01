# https://atcoder.jp/contests/abc141/tasks/abc141_b

s = input()

odd = s[0::2]
even = s[1::2]

if "L" not in odd and "R" not in even:
  print("Yes")
else:
  print("No")