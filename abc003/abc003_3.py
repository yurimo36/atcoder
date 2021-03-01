# https://atcoder.jp/contests/abc003/tasks/abc003_3

n, k = map(int,input().split())
r = list(map(int,input().split()))
ans = 0.0

r.sort(reverse=True)
r = r[:k]
r.sort()

for i in r:
  ans = (ans + i) / 2 
  
print(ans)