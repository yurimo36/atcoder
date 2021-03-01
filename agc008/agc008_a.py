# https://atcoder.jp/contests/agc008/tasks/agc008_a

x, y = map(int,input().split())

if x*y < 0: #異符号→反転可能性あり
    print(abs(abs(x)-abs(y))+1)

elif x*y == 0:
    if x <= y:
        print(y-x)
    else:
        print(x-y+1)

else: #同符号→反転可能性なし
    if x <= y:
        print(y-x)
    else:
        print(x-y+2)