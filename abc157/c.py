# https://atcoder.jp/contests/abc157/tasks/abc157_c

n, m = map(int,input().split())
ans = [-1] * n
flag = 1

for i in range(m):
  s, c = map(int,input().split())
  if ans[s-1] == -1 or ans[s-1] == c: #まだ値が入っていないか同じ値が
    ans[s-1] = c
  else: #同じ桁に複数の条件が重複するのはだめ
    flag = 0

if ans[0] == 0 and n != 1: #最初の桁0はダメ
  flag = 0

if flag == 0:
  print(-1)

else:
  for i in range(n):
    if ans[i] == -1:
        if i == 0 and n != 1:
            ans[i] = 1
        else:
            ans[i] = 0
    print(ans[i], end ="")