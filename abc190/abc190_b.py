# https://atcoder.jp/contests/abc190/tasks/abc190_b

n, s, d = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]

for l in li:
  if l[0] < s and l[1] > d:
    print("Yes")
    exit()

print("No")
