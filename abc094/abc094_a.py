# https://atcoder.jp/contests/abc094/tasks/abc094_a

a, b, x = map(int,input().split())
 
if x < a or a+b < x:
  print("NO")
else:
  print("YES")