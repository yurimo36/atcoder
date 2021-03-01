# https://atcoder.jp/contests/abc139/tasks/abc139_c

n = int(input())
h = list(map(int,input().split()))
x = []
y = 0

if n == 1:
    print(0)

else:
    for i in range(n-1):
        if h[i] < h[i+1]:
            y = 0
        else:
            y = y + 1
        x.append(y)
 
    print(max(x))