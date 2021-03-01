# https://atcoder.jp/contests/abc060/tasks/arc073_a

x, y = map(int,input().split())
li = list(map(int,input().split()))
ans = y

for i in range(1,x):
    z = li[i] - li[i-1]
    if z < y:
        ans += z
    else:
        ans += y

print(ans)