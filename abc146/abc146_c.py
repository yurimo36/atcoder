# https://atcoder.jp/contests/abc146/tasks/abc146_c

a, b, x = map(int,input().split())
min = 0
max = 10**9+1

while abs(max-min) > 1: #二分探索
    mid = (max+min)//2
    if mid*a + len(str(mid))*b <= x: #まだ買えるなら
        min = mid
    else:
        max = mid

print(min)