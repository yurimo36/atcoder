# https://atcoder.jp/contests/arc008/tasks/arc008_1

n = int(input())
x = n%10
ans = n//10*100

if x > 6:
  ans += 100
else:
  ans += x*15

print(ans)