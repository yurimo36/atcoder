# https://atcoder.jp/contests/abc148/tasks/abc148_d

n = int(input())
a = list(map(int,input().split()))
x = 1
ans = 0

for i in a:
    if i == x:
        ans += 1
        x += 1

if ans == 0:
    print(-1)
else:
    print(len(a)-ans)