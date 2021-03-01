# https://atcoder.jp/contests/abc164/tasks/abc164_b

a, b, c, d = map(int,input().split())

while True:
    c -= b #高橋くんの攻撃
    if c <= 0:
        print("Yes")
        exit()
    a -= d
    if a <= 0:
        print("No")
        exit()