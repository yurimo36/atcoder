# https://atcoder.jp/contests/abc136/tasks/abc136_b

n = int(input())
ans = 0
m = n
x = 1

while m >= 10: #nの桁数を求める
  m = m / 10
  x = x + 1

for i in range(1,x+1):
  if i == x and i%2 == 1: #最後の奇数桁だったら
    ans = ans + n - 10**(i-1) + 1
  elif i%2 == 0: #偶数桁だったら
      continue
  else: #最後の桁意外の奇数だったら
    ans = ans + 9 * 10**(i-1)

print(ans)