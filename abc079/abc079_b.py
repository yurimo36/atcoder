# https://atcoder.jp/contests/abc079/tasks/abc079_b

n = int(input())
x = 2
y = 1

if n == 1:
    ans = 1

for i in range(n-1):
    ans = x + y
    x = y
    y = ans

print(ans)