# https://atcoder.jp/contests/abc064/tasks/abc064_c

n = int(input())
li = list(map(int,input().split()))
color = [0]*8
x = 0

for i in li:
    if i < 400:
        color[0] += 1
    elif i < 800:
        color[1] += 1
    elif i < 1200:
        color[2] += 1
    elif i < 1600:
        color[3] += 1
    elif i < 2000:
        color[4] += 1
    elif i < 2400:
        color[5] += 1
    elif i < 2800:
        color[6] += 1
    elif i < 3200:
        color[7] += 1
    else:
        x += 1

ans = 8-color.count(0)
x += ans
if ans == 0:
    ans += 1
print(ans, x)