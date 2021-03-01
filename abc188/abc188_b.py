# https://atcoder.jp/contests/abc188/tasks/abc188_b

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
naiseki = 0

for i in range(n):
    naiseki += a[i]*b[i]

if naiseki == 0:
    print("Yes")
else:
    print("No")