# https://atcoder.jp/contests/agc004/tasks/agc004_a

a, b, c = map(int,input().split())

if a%2 == 0 or b%2 == 0 or c%2 == 0:
    print(0)
else:
    print(a*b*c//max(a,b,c))