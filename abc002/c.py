# https://atcoder.jp/contests/abc002/tasks/abc002_3

x, y, a, b, c, d = map(int,input().split())

a = a - x
c = c - x
b = b - y
d = d - y

print(abs(a*d-b*c)/2)