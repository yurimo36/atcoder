# https://atcoder.jp/contests/abc153/tasks/abc153_d

h = int(input())
i = h
x = 0

while h >= 2:
  h = h / 2
  x = x + 1 #2のなんじょうかを求める

print(2**(x+1) - 1)