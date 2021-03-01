# https://atcoder.jp/contests/abc090/tasks/abc090_b

x, y = map(int,input().split())
ans = 0

for i in range(x,y+1):
    if str(i) == str(i)[::-1]:
        ans += 1

print(ans)