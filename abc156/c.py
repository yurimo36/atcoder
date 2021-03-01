# https://atcoder.jp/contests/abc156/tasks/abc156_c

n = int(input())
x = list(map(int,input().split()))
a = max(x)
b = min(x)
y = 0
ans = 10000000

for i in range (b,a+1): #住民がいる間で
  y = 0 #初期化
  for j in x: #体力の総和を計算
    y = y + (j-i)**2
  if y < ans:
    ans = y

print(ans)
