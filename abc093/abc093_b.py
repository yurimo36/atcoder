# https://atcoder.jp/contests/abc093/tasks/abc093_b

a, b, k = map(int,input().split())

if b-a+1 < k*2:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,a+k):
        print(i)
    for i in range(b+1-k,b+1):
        print(i)