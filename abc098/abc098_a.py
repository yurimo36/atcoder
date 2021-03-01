# https://atcoder.jp/contests/abc098/tasks/abc098_a

x, y = map(int,input().split())
print(max(x+y, x-y, x*y))