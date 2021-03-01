# https://atcoder.jp/contests/abc167/tasks/abc167_b

a, b, c, k = map(int,input().split())
ans = 0

if a < k:
    ans = a
    k -= a
    if b < k:
        k -= b
        if c < k:
            ans -= c
        else:
            ans -= k
else:
    ans = k

print(ans)