# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_b

h, w = map(int,input().split())
li = [list(input()) for i in range(h)]
ans = 0

for i in range(h):
  for j in range(w-1):
    if li[i][j] == li[i][j+1] == ".":
      ans += 1

for i in range(w):
  for j in range(h-1):
    if li[j][i] == li[j+1][i] == ".":
      ans += 1

print(ans)
