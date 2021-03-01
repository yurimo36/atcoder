# https://atcoder.jp/contests/abc080/tasks/abc080_b

s = int(input())
x = 0
 
for i in str(s):
  x += int(i)
 
if s%x == 0:
  print("Yes")
else:
  print("No")