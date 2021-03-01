# https://atcoder.jp/contests/abc104/tasks/abc104_b

s = list(input())

if s[0] == "A" and s[2:-1].count("C") == 1:
  s.remove("A")
  s.remove("C")
  for c in s:
    if c.isupper() == True:
      print("WA")
      exit()
    else:
      continue
  print("AC")

else:
  print("WA")