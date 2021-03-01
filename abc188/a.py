# https://atcoder.jp/contests/abc188/tasks/abc188_a

x, y = map(int,input().split())

if min(x,y)+3 <= max(x,y):
    print("No")
else:
    print("Yes")
