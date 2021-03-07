# https://atcoder.jp/contests/abc194/tasks/abc194_c

n = int(input())
li = list(map(int,input().split()))
ans = 0
x = 0

for i in li:
  ans -= 2*x*i
  ans += i**2 * (n-1)
  x += i

print(ans)
