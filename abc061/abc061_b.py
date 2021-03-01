# https://atcoder.jp/contests/abc061/tasks/abc061_b

n, m = map(int,input().split())
ans = [0]*n

for i in range(m):
    x, y = map(int,input().split())
    ans[x-1] += 1
    ans[y-1] += 1

for i in ans:
    print(i)