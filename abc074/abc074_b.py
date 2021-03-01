# https://atcoder.jp/contests/abc074/tasks/abc074_b

n = int(input())
k = int(input())
x = list(map(int,input().split()))
ans = 0

for i in x:
    ans += min(abs(i-k),i)*2

print(ans)