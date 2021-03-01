# https://atcoder.jp/contests/arc012/tasks/arc012_2

n, a, b, l = map(int,input().split())

for i in range(n):
    l = l/a*b

if l < 10**-7:
    print(0)
else:
    print(l)