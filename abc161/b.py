# https://atcoder.jp/contests/abc161/tasks/abc161_b

n, m = map(int,input().split())
a = list(map(int,input().split()))
 
a.sort(reverse=True)
x = sum(a)
 
if a[m-1] < x/(4*m):
  print("No")
else:
  print("Yes")