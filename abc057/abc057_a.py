# https://atcoder.jp/contests/abc057/tasks/abc057_a

x, y = map(int,input().split())
z = x+y
print(z) if z < 24 else print(z-24)