# https://atcoder.jp/contests/abc111/tasks/abc111_b

n = int(input())
x = int(str(n)[0])
y = x*100 + x*10 + x #100の位のゾロ目

if n <= y :
  print(y)
else:
  print(y+111)