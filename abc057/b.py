# https://atcoder.jp/contests/abc057/tasks/abc057_b

n, m = map(int,input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(m):
    b.append(list(map(int,input().split())))

for i in range(n):
    ans = 10000000000000
    for j in range(m):
        x = abs(a[i][0]-b[j][0]) + abs(a[i][1]-b[j][1])
        if x < ans:
            ans = x
            y = j
    print(y+1)