# https://atcoder.jp/contests/abc119/tasks/abc119_b

n = int(input())
ans = 0.0

for i in range(n):
    x = input().split()
    if x[1] == "JPY":
        ans += float(x[0])
    else:
        ans += float(x[0])*380000

print(ans)