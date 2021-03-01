# https://atcoder.jp/contests/tenka1-2012-qualB/tasks/tenka1_2012_5

x, y, z = map(int,input().split())

for i in range(1,128):
    if i%3 == x and i%5 == y and i%7 == z:
        print(i)