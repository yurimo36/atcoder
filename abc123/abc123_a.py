# https://atcoder.jp/contests/abc123/tasks/abc123_a

n = [int(input()) for i in range(5)]
k = int(input())

if max(n) - min(n) > k:
  print(":(")
else:
  print("Yay!")