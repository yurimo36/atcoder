# https://atcoder.jp/contests/caddi2018b/tasks/caddi2018b_b

n, h, w = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]
ans = 0

for l in li:
    if l[0] >= h and l[1] >= w:
        ans += 1

print(ans)