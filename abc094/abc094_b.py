# https://atcoder.jp/contests/abc094/tasks/abc094_b

n, m, x = map(int,input().split())
a = list(map(int,input().split()))
y = 0
z = 0

for i in a:
    if i < x:
        y += 1
    else:
        z += 1

print(min(y,z))