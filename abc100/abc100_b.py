# https://atcoder.jp/contests/abc100/tasks/abc100_b

x, y = map(int,input().split())

if x == 0:
    if y == 100:
        print(101)
    else:
        print(y)
if x == 1:
    if y == 100:
        print(10100)
    else:
        print(y*100)
if x == 2:
    if y == 100:
        print(1010000)
    else:
        print(y*10000)