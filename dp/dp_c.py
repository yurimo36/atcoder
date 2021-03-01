# https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
dp = [[0 for i in range(3)] for j in range(n+1)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k: #同じことを2日連続はできない
                continue
            dp[i+1][k] = max(dp[i+1][k], li[i][k] + dp[i][j])

print(max(dp[n]))