# https://atcoder.jp/contests/abc068/tasks/abc068_b

n = int(input())
ans = 1

while ans <= n:
  ans *= 2

print(ans//2)