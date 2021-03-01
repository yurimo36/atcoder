# https://atcoder.jp/contests/abc101/tasks/abc101_b

n = input()
x = 0
for i in n:
  x += int(i)

if int(n)%x == 0:
  print("Yes")
else:
  print("No")