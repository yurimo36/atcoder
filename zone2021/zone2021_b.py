# https://atcoder.jp/contests/zone2021/tasks/zone2021_b

def calc_slope_intersept(x1, y1, x2, y2):
  a = (y1 - y2) / (x1 - x2)
  b = y1 - a * x1
  return b

n, d, h = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]

ans = 0
for l in li:
  ans = max(ans, calc_slope_intersept(l[0], l[1], d, h))

print(ans)
