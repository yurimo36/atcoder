# https://atcoder.jp/contests/abc135/tasks/abc135_c

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0

for i in range(n):
    if a[i] >= b[i]:
        ans += b[i]
    else:
        x = min(b[i], a[i]+a[i+1])
        a[i+1] = a[i+1]-x+a[i]
        ans += x

print(ans)