# https://atcoder.jp/contests/abc040/tasks/abc040_c

n = int(input())
h = list(map(int,input().split()))
ans = [10**6]*n
ans[0] = 0

for i in range(1,n):
    if i == 1:
        ans[i] = ans[i-1] + abs(h[i]-h[i-1])
    else:
        ans[i] = min(ans[i-1]+abs(h[i]-h[i-1]),ans[i-2]+abs(h[i]-h[i-2]))

print(ans[n-1])

