# https://atcoder.jp/contests/agc002/tasks/agc002_a

a, b = map(int,input().split())

if a*b <= 0: #異符号もしくは0を含むなら
    print("Zero")

elif a > 0: #両方正なら
    print("Positive")

else: #両方負なら
    if (b-a)%2==0:
        print("Negative")
    else:
        print("Positive")