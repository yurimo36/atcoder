# https://atcoder.jp/contests/abc087/tasks/abc087_b

a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0

for i in range(0,a+1):
  for j in range(0,b+1):
    for k in range(0,c+1):
      y = i*500 + j*100 + k*50
      if x == y:
        ans += 1

print(ans)