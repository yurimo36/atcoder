# https://atcoder.jp/contests/abc168/tasks/abc168_c

import math

a, b, h, m = map(int,input().split())

#まず間の角度を求める
x = h*30+m/2
y = m*6
kakudo = max(x,y)-min(x,y)
kakudo = min(kakudo,360-kakudo)

ans = (a**2 + b**2 - 2*a*b*math.cos(math.radians(kakudo)))**0.5

print(ans)