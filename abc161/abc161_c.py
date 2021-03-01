# https://atcoder.jp/contests/abc161/tasks/abc161_c

n, k = map(int,input().split())

if n > k:
    n = min(n%k, k-n%k)
else:
    n = min(n, abs(n-k)) #に置き換えられる

print(n)