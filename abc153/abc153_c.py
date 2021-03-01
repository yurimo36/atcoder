# https://atcoder.jp/contests/abc153/tasks/abc153_c

n, k = map(int,input().split())
h = list(map(int,input().split()))
h.sort(reverse=True)
ans = 0

if k > n:
  ans = 0
  
else:
  ans = sum(h) - sum(h[:k])
  
print(ans)