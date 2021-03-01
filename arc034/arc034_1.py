# https://atcoder.jp/contests/arc034/tasks/arc034_1

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
ans = 0

for l in li:
    x = sum(l[:4]) + l[4]*11/90
    if x > ans:
        ans = x

print(ans)