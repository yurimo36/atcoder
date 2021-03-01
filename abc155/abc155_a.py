# https://atcoder.jp/contests/abc155/tasks/abc155_a

a, b ,c = map(int,input().split())

if a==b and b!=c:
  print("Yes")
elif c==b and b!=a:
  print("Yes")
elif a==c and b!=c:
  print("Yes")
else:
  print("No")