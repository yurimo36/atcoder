# https://atcoder.jp/contests/apc001/tasks/apc001_a

x, y = map(int,input().split())
 
if x%y == 0:
    print(-1)
else:
    print(x)