# https://atcoder.jp/contests/abc199/tasks/abc199_b

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

x = max(a)
y = min(b)

if x > y:
  print(0)
else:
  print(y-x+1)
