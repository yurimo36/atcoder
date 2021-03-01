# https://atcoder.jp/contests/abc054/tasks/abc054_a

x, y = map(int,input().split())

if x == y:
    print("Draw")
elif x == 1:
    print("Alice")
elif y == 1:
    print("Bob")
elif x > y:
    print("Alice")
else:
    print("Bob")