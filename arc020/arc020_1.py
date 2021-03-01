# https://atcoder.jp/contests/arc020/tasks/arc020_1

x, y = map(int,input().split())
x = abs(x)
y = abs(y)

if x < y:
    print("Ant")
elif x > y:
    print("Bug")
else:
    print("Draw")