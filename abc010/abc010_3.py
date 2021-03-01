# https://atcoder.jp/contests/abc010/tasks/abc010_3

a, b, c, d , t, v = map(int,input().split())
n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]

for li in xy:
    x = li[0]
    y = li[1]
    z = ((a-x)**2 + (b-y)**2)**0.5 + ((c-x)**2 + (d-y)**2)**0.5
    if z <= t*v:
        print("YES")
        exit()

print("NO")