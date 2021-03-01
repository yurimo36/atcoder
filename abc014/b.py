# https://atcoder.jp/contests/abc014/tasks/abc014_2

x, y = map(int,input().split())
li = list(map(int,input().split()))
ans = 0
b = format(y, 'b')
b = str(b).rjust(x,'0')

for i in range(x):
    if b[i] == "1":
        ans += li[x-1-i]

print(ans)