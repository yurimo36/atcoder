# https://atcoder.jp/contests/abc125/tasks/abc125_b

n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0

for i in range(n):
    if v[i] > c[i]:
        ans = ans + v[i] - c[i]

print(ans)