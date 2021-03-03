# https://atcoder.jp/contests/abc187/tasks/abc187_b

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
ans = 0

for i in range(n):
    for j in range(i+1, n):
        x1 = int(li[i][0])
        y1 = int(li[i][1])
        x2 = int(li[j][0])
        y2 = int(li[j][1])
        a = (y2-y1) / (x2-x1)
        if -1 <= a <= 1:
            ans += 1

print(ans)
