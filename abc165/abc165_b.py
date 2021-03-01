# https://atcoder.jp/contests/abc165/tasks/abc165_b

n = 100
x = int(input())
ans = 0

while n < x:
    n = int(n*1.01)
    ans += 1

print(ans)