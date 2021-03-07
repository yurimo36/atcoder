# https://atcoder.jp/contests/abc190/tasks/abc190_c

n, m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]
k = int(input())
cd = [list(map(int,input().split())) for i in range(k)]
ans = 0

# 全パターンを試す
for i in range(2 ** k):
  x = 0
  li = []
  for j in range(k):
    if ((i >> j) & 1): #フラグが立っていたら
      li.append(cd[j][0])
    else:
      li.append(cd[j][1])
  for pattern in ab:
    if pattern[0] in li and pattern[1] in li:
      x += 1
  if x > ans:
    ans = x

print(ans)
