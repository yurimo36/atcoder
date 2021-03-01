# https://atcoder.jp/contests/abc118/tasks/abc118_b

n, m = map(int,input().split())
ans = [1]*m

for i in range(n):
    x = list(map(int,input().split()))
    x.pop(0)
    for j in range(1,m+1):
        if j not in x:
            ans[j-1] = 0

print(ans.count(1))