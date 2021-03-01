# https://atcoder.jp/contests/abc021/tasks/abc021_a

n = int(input())
a = n%2
b = int(n/2)

print(a+b)
for i in range(a):
  print(1)
for i in range(b):
  print(2)