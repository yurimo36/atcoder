# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_b

a, b, c = map(int,input().split())
k = int(input())

for i in range(k):
  if a >= b:
    b *= 2
  else:
    c *= 2

if a < b < c:
  print("Yes")
else:
  print("No")
