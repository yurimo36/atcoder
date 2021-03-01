# https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_a

s = input()
if len(s)%2 == 1:
  print("No")
  exit()
  
for i in range(len(s)):
  if i%2 == 0:
    if s[i] != "h":
      print("No")
      exit()
  else:
    if s[i] != "i":
      print("No")
      exit()
print("Yes")