# https://atcoder.jp/contests/abc166/tasks/abc166_c

n, m = map(int,input().split())
h = list(map(int,input().split()))
ans = [1]*n #いい展望台のところは1にする
li = []
for i in range(m):
    li.append(list(map(int,input().split())))

for x in li:
    y = h[x[0]-1]
    z = h[x[1]-1]
    if y <= z:
        ans[x[0]-1] = 0
    if z <= y:
        ans[x[1]-1] = 0

print(ans.count(1))