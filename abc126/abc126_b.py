# https://atcoder.jp/contests/abc126/tasks/abc126_b

s = input()

a = int(s[:2])
b = int(s[2:])

if (a == 00 or a > 12) and b <= 12 and b >= 1:
  print("YYMM")
elif a <= 12 and a >= 1 and (b == 00 or b > 12):
  print("MMYY")
elif a <= 12 and a >= 1 and b <= 12 and b >= 1:
  print("AMBIGUOUS")
else:
  print("NA")