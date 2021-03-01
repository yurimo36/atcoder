# https://atcoder.jp/contests/abc126/tasks/abc126_c

n, k =  map(int,input().split())
ans = 0.0

for i in range(1,n+1):
  x = 0
  while i < k:
    i = i * 2
    x = x + 1
  ans = ans + 1/n * (1/2)**x
  
print(ans)