# https://atcoder.jp/contests/abc024/tasks/abc024_a

a, b, c, k = map(int,input().split())
s, t = map(int,input().split())

if s+t >= k:
    print(a*s + b*t - c*(s+t))
else:
    print(a*s + b*t)