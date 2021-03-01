# https://atcoder.jp/contests/abc110/tasks/abc110_b

n, m, x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = max(a)+1
d = min(b)
e = 0

if c > d:
    print("War")
else:
    for i in range(c,d+1):
        if x < i and i <= y:
            print("No War")
            e = 1
            break
    if e == 0:
        print("War")