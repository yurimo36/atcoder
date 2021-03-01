# https://atcoder.jp/contests/arc028/tasks/arc028_1

n, a, b = map(int,input().split())

while True:
    n -= a
    if n < 1:
        print("Ant")
        break
    n -= b
    if n < 1:
        print("Bug")
        break