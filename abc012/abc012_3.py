# https://atcoder.jp/contests/abc012/tasks/abc012_3

n = 2025 - int(input())
ans = []

for i in range(1,10):
  for j in range(1,10):
    if i*j == n:
      ans.append([i,j])

for i in ans:
  print(str(i[0]) + " x " + str(i[1]))