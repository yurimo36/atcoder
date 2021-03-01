# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c

x = int(input())
y = x//100
z = x%100

if z > y*5:
    print(0)
else:
    print(1)