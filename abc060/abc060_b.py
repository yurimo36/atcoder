# https://atcoder.jp/contests/abc060/tasks/abc060_b

x, y, z = map(int,input().split())
li = []

for i in range(y):
    li.append((x*i)%y)

if z in li:
    print("YES")
else:
    print("NO")