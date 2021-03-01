# https://atcoder.jp/contests/abc131/tasks/abc131_a

s = input()
x = 0

for i in range(len(s)-1):
  if s[i] == s[i+1]:
    x = 1

if x == 0:
  print("Good")
else:
  print("Bad")