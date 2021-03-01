# https://atcoder.jp/contests/abc003/tasks/abc003_2

s = input()
t = input()
x = 0

for i in range(len(s)):
  if s[i] == t[i]:
    continue
  elif s[i] == "@" and (t[i] == "a" or t[i] == "t" or t[i] == "c" or t[i] == "o" or t[i] == "d" or t[i] == "e" or t[i] == "r"):
    continue
  elif t[i] == "@" and (s[i] == "a" or s[i] == "t" or s[i] == "c" or s[i] == "o" or s[i] == "d" or s[i] == "e" or s[i] == "r"):
    continue
  else:
    x = 1
    break
    
if x == 0:
  print("You can win")
else:
  print("You will lose")