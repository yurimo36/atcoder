# https://atcoder.jp/contests/abc158/tasks/abc158_c

a ,b = map(int,input().split())
ans = 100000000000

x = int(a / 0.08) #最小値を設定
y = int((b+10) / 0.1) #最大値を設定

z = 0

for i in range(x, y):
  if int(i * 0.08) == a and int(i * 0.1)  == b and i < ans:
    ans = i
    z = 1

if z == 1:
  print(ans)
else:
  print(-1)