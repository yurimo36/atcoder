# https://atcoder.jp/contests/abc015/tasks/abc015_2

n = int(input())
a = list(map(int,input().split()))
s = sum(a)
n = n - a.count(0)

if s%n == 0:
  print(int(s/n))
else:
  print(int(s/n)+1)