# https://atcoder.jp/contests/abc154/tasks/abc154_d

x, y = map(int,input().split())
p = list(map(int,input().split()))
ans = 0

for i in range(x-y+1):
    if i == 0:
        z = sum(p[:y])
    else:
        z = z - n + p[i+y-1]
    n = p[i]
    if z > ans:
        ans = z

print((ans+y)/2)