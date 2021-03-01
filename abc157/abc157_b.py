# https://atcoder.jp/contests/abc157/tasks/abc157_b

a=[]
for i in range(3):
  a.append(list(map(int,input().split())))
n = int(input())
x = 0

for i in range(n):
  b = int(input())
  for j in range(3):
    for k in range(3):
      if a[j][k] == b:
        a[j][k] = 0

if (a[0][0] == 0 and a[2][2] == 0 and a[1][1] == 0) or (a[0][2] == 0 and a[2][0] == 0 and a[1][1] == 0): #斜めに揃っていたら
  print("Yes")
  x = 1
for i in range(3):
  if a[i][0] == 0 and a[i][1] == 0 and a[i][2] == 0 and x == 0: #横に揃っていたら
    print("Yes")
    x = 1
    break
  elif a[0][i] == 0 and a[1][i] == 0 and a[2][i] == 0 and x == 0: #縦に揃っていたら
    print("Yes")
    x = 1
    break
if x == 0:
  print("No")