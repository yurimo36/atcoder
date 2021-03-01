# https://atcoder.jp/contests/agc020/tasks/agc020_a

n, a, b = map(int,input().split())

if (a-b)%2 == 0:
    print("Alice")
else:
    print("Borys")