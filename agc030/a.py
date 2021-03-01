# https://atcoder.jp/contests/agc030/tasks/agc030_a

a, b, c = map(int,input().split())

if a+b >= c:
    ans = b+c
else:
    ans = b+a+b+1

print(ans)