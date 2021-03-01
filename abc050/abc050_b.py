# https://atcoder.jp/contests/abc050/tasks/abc050_b

n = int(input())
t = list(map(int,input().split()))
m = int(input())
ans = [sum(t)]*m

for i in range(m):
    x, y = map(int,input().split())
    ans[i] = ans[i] + y - t[x-1]

for i in ans:
    print(i)