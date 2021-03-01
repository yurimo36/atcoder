# https://atcoder.jp/contests/abc037/tasks/abc037_b

n, q = map(int,input().split())
ans = [0]*n

for i in range(q):
  x, y, z = map(int,input().split())
  for j in range(x-1,y):
    ans[j] = z
    
for i in ans:
  print(i)