# https://atcoder.jp/contests/abc103/tasks/abc103_a

x, y, z = map(int,input().split())
l = []

l.append(abs(x-y))
l.append(abs(z-y))
l.append(abs(x-z))

print(sum(l)-max(l))