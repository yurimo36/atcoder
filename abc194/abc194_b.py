# https://atcoder.jp/contests/abc194/tasks/abc194_b

n = int(input())
a = []
b = []
c = 10**6

for i in range(n):
  x, y = map(int,input().split())
  a.append(x)
  b.append(y)
  if x+y < c:
    c = x+y

x = min(a)
y = min(b)

if a.index(x) != b.index(y):
  print(max(x,y))

else:
  a.sort()
  b.sort()
  print(min(c, max(x,b[1]), max(y,a[1])))
