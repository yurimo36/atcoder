# https://atcoder.jp/contests/abc087/tasks/arc090_a

n = int(input())
c = []
c.append(list(map(int,input().split())))
c.append(list(map(int,input().split())))
ans = 0

for i in range(n):
    x = sum(c[0][:i+1]) + sum(c[1][i:])
    if x > ans:
        ans = x

print(ans)