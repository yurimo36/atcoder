# https://atcoder.jp/contests/abc095/tasks/abc095_b

n, x = map(int,input().split())
ans = n

m = [int(input()) for i in range(n)]

x -= sum(m)
ans += x//min(m)
print(ans)