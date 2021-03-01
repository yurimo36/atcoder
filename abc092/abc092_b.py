# https://atcoder.jp/contests/abc092/tasks/abc092_b

n = int(input())
d, ans = map(int,input().split())
a = [int(input()) for i in range(n)]

for i in a:
    j = 1
    while j <= d:
        ans += 1
        j += i

print(ans)