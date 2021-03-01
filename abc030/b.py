# https://atcoder.jp/contests/abc030/tasks/abc030_b

n, m = map(int,input().split())

n %= 12
x = n*30+m/2
y = m*6

ans = max(x,y)-min(x,y)
print(min(ans,360-ans))