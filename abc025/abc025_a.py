# https://atcoder.jp/contests/abc025/tasks/abc025_a

s = list(input())
n = int(input())

x = (n-1)//5
y = (n-1)%5

ans = s[x] + s[y]
print(ans)